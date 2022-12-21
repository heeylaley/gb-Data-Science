-- 01.11. Автоматизируем задания для удобства последующего использования


-- 1. Представление полной истории болезни (ИБ) на пациентов
CREATE OR REPLACE VIEW v_patients
AS
SELECT
p.id,
p.name AS `ФИО`,
p.age AS `Возраст`,
p.passport AS `Паспортные данные`,
p.address AS `Адрес`,
p.arr_date AS `Дата поступления`,
DATE_ADD(p.arr_date, INTERVAL p.day_staying DAY) AS `Дата выписки`,
IF(p.sickleave=0, 'Нет', 'Да') AS  `Требуется ли больничный лист`,
s.name AS `Лечащий врач`,
mr.room AS `Палата`,
dv.disease_name AS `Диагноз`,
p.concomitant AS `Сопутствующее(-ие) забоелвание(-ия)`,
dv.complaints AS `Жалобы`,
dv.anamnesis AS `Анамнез`,
IF(pc.basic=0, 'Удовлетворительное', 'Тяжелое') `Состояние больного`,
pc.temp AS `toC`,
pc.body AS `Телосложение`,
IF(pc.lymphnodes=0, 'Не увеличены', 'Увеличены') AS `Л/у`,
IF(pc.muscskel=0, 'Норма', 'Патология') AS `Скелетно-мышечная система`,
IF(pc.skin=0, 'Норма', 'Патология') AS `Кожные покровы`,
dv.status_localis AS `Локальный статус`,
IF(pc.heart=0, 'Норма', 'Патология') AS `Сердечно-сосудистая система`,
IF(pc.lungs=0, 'Норма', 'Патология') AS `Дыхательная система`,
IF(pc.stomach=0, 'Норма', 'Патология') AS `Живот`,
IF(pc.urinary=0, 'Отрицательный', 'Положительный') AS `Симптом Пастернацкого`,
dv.strategy AS `План обследования`,
(SELECT CONCAT(drug_name, ' ', form, ' ', times, ' раза в ', freq) FROM medicaments m
		WHERE m.id = (SELECT t.drug_id FROM treatment t WHERE t.disease_id = p.diagnosis AND t.number_treatment = 1)) AS `Терапия 1`,
(SELECT CONCAT(drug_name, ' ', form, ' ', times, ' раза в ', freq) FROM medicaments m
		WHERE m.id = (SELECT drug_id FROM treatment WHERE disease_id = p.diagnosis AND number_treatment = 2)) AS `Терапия 2`,
(SELECT CONCAT(drug_name, ' ', form, ' ', times, ' раза в ', freq) FROM medicaments m
		WHERE m.id = (SELECT drug_id FROM treatment WHERE disease_id = p.diagnosis AND number_treatment = 3)) AS `Терапия 3`,
(SELECT CONCAT(drug_name, ' ', form, ' ', times, ' раза в ', freq) FROM medicaments m
		WHERE m.id = (SELECT drug_id FROM treatment WHERE disease_id = p.diagnosis AND number_treatment = 4)) AS `Терапия 4`,
pc.epicrisis AS `Эпикриз`

FROM patients p
JOIN disease_vocab dv ON dv.id = p.diagnosis
JOIN med_rooms mr ON (mr.patient_id = p.id AND status = 1)
JOIN staff s ON s.id = p.doctor_id
JOIN patient_condition pc ON pc.id = p.id;


SELECT * FROM v_patients;







-- 2. Представление для запросов страховых компаний или с работы
CREATE OR REPLACE VIEW v_for_ensurance
AS
SELECT
`Паспортные данные`,
`Дата поступления`,
`Дата выписки`,
`Требуется ли больничный лист`
FROM v_patients;

SELECT * FROM v_for_ensurance;






/* 3. Права работников из страховых/места работы пациента для просмотра информации
 	о листе нетрудоспособности. Все остальные данные будут недоступны по причине
 	врачебной тайны
 */

CREATE USER EnsurancyAgent;
GRANT SELECT ON v_for_ensurance.* TO EnsurancyAgent;








-- 4. Триггеры

-- 4.1 Д/р пациента
-- 4.1.1
DROP TRIGGER IF EXISTS dvo.check_arrival_date_bi;
USE dvo;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER `check_arrival_date_bi` BEFORE INSERT ON `patients` FOR EACH ROW BEGIN
	IF NEW.arr_date > current_date() THEN
		SET NEW.arr_date = current_date();
	END IF;
END$$
DELIMITER ;




-- 4.1.2
DROP TRIGGER IF EXISTS dvo.check_arrival_date_bu;
USE dvo;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER `check_arrival_date_bu` BEFORE UPDATE ON `patients` FOR EACH ROW BEGIN
	IF NEW.arr_date > current_date() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Некорректная дата';
	END IF;
END$$
DELIMITER ;





-- 4.2 категория executor на процедуру '232'
-- 4.2.1
DROP TRIGGER IF EXISTS dvo.check_executor_bi;
USE dvo;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER `check_executor_bi` BEFORE INSERT ON `procedure_sch` FOR EACH ROW BEGIN
	IF NEW.procedure_type = 232 AND NEW.executor NOT IN (SELECT id FROM staff WHERE cat = 1) THEN
		SET NEW.executor = 1;
	END IF;
END$$
DELIMITER ;


-- 4.2.2
DROP TRIGGER IF EXISTS dvo.check_executor_bu;
USE dvo;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER `check_executor_bu` BEFORE UPDATE ON `procedure_sch` FOR EACH ROW BEGIN
	IF NEW.procedure_type = 232 AND NEW.executor NOT IN (SELECT id FROM staff WHERE cat = 1) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Брать биопсию может только врач';
	END IF;
END$$
DELIMITER ;







-- 5. Процедура эпикриза
DROP PROCEDURE IF EXISTS dvo.epicrisis;

DELIMITER $$
$$
CREATE PROCEDURE dvo.epicrisis()
BEGIN
	
	UPDATE patient_condition
	SET epicrisis = 'Пациент успешно прошeл лечение и выписан' -- для простоты в таком варианте ))
	WHERE id IN (SELECT id AS the_ones_who_left FROM dvo.patients
				 WHERE date_add(arr_date, INTERVAL day_staying DAY) < current_date());
	
END$$
DELIMITER ;


CALL epicrisis();

-- Проверяем
SELECT * FROM v_patients vp WHERE `Эпикриз` IS NOT NULL






-- 6. Процедура добавления новых пациентов
DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `dvo`.`add_patient`(name VARCHAR(32), age TINYINT, passport VARCHAR(32),
	address VARCHAR(255), arr_date DATE, day_staying TINYINT, diagnosis BIGINT, concomitant VARCHAR(255),
	sickleave BIT, doctor_id BIGINT, medsestra BIGINT, room_num BIGINT, OUT trans_res VARCHAR(255))
BEGIN
	DECLARE `_rollback` BIT DEFAULT 0;
	DECLARE code varchar(100);
	DECLARE error_string varchar(100);
	DECLARE last_patient_id BIGINT;
	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
	BEGIN
 		SET `_rollback` = 1;
 		GET stacked DIAGNOSTICS CONDITION 1
			code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
		SET trans_res = CONCAT('Ошибка: ', code, ' Текст ошибки: ', error_string);
	END;


	START TRANSACTION;
	-- Данные пациента
	INSERT INTO patients (name, age, passport, address, arr_date, day_staying, diagnosis, concomitant, sickleave,
	 					doctor_id)
	VALUES (name, age, passport, address, arr_date, day_staying, diagnosis, concomitant, sickleave, doctor_id);
	
	SET last_patient_id = last_insert_id();

	-- Особенности ИБ
	INSERT INTO patient_condition (id)
	VALUES (last_patient_id);

	IF (SELECT concomitant FROM patients WHERE id = last_patient_id) LIKE '%гипер%' THEN		-- Артериальная гипертензия
	UPDATE patient_condition SET heart = 1 WHERE id = last_patient_id;
	END IF;
	
	
	IF (SELECT concomitant FROM patients WHERE id = last_patient_id) LIKE '%желуд%' THEN		-- Язвенная болезнь желудка
	UPDATE patient_condition SET stomach = 1 WHERE id = last_patient_id;
	END IF;


	IF (SELECT concomitant FROM patients WHERE id = last_patient_id) LIKE '%обстр%' THEN		-- Хроническая обструктивная болезнь лёгких
	UPDATE patient_condition SET heart = 1 WHERE id = last_patient_id;
	UPDATE patient_condition SET lungs = 1 WHERE id = last_patient_id;
	END IF;
	

	-- Заселяем в палату
	INSERT INTO med_rooms (date_of_status_change, room, patient_id, status)
	VALUES (arr_date, room_num, last_patient_id, 1);


	-- Выписываем
	INSERT INTO med_rooms (date_of_status_change, room, patient_id, status)
	VALUES (DATE_ADD(arr_date, INTERVAL day_staying DAY), room_num, last_patient_id, 0);


	-- Обязательная процедура - взятие крови и гистологический биоптат при определенных заболеваниях (id болезней 1, 3, 7)
	-- Кровь
	INSERT INTO procedure_sch (procedure_date, procedure_type, patient_id, executor)
	VALUES (DATE_ADD(arr_date, INTERVAL 1 DAY), 11, last_patient_id, medsestra);


	-- Биоптат
	IF (SELECT (SELECT diagnosis FROM patients WHERE id = last_patient_id) IN (1, 3, 7)) = 1 THEN
		INSERT INTO procedure_sch (procedure_date, procedure_type, patient_id, executor)
		VALUES (DATE_ADD(arr_date, INTERVAL 2 DAY), 232, last_patient_id, doctor_id);
	END IF;
	
	
	IF `_rollback` THEN
		SET trans_res = 'ROLLBACK';
		ROLLBACK;
	ELSE
		SET trans_res = 'COMMIT';
		COMMIT;
	END IF;
END$$
DELIMITER ;


-- Проверяем
CALL add_patient('Лимонов Лимон Лимонович', 33, '333', 'ул. Лимонная, 33', '2022-11-01', 14, 3, 'Язвенная болезнь желудка', 0, 3, 6, 5, @trans_res);
SELECT @trans_res;





-- 7. Процедура суммарных трат
DROP PROCEDURE IF EXISTS dvo.expenses;

DELIMITER $$
$$
CREATE PROCEDURE dvo.expenses(desired_month SMALLINT)
BEGIN
	
	SELECT SUM(`sum_start`) AS 'суммарные затраты'
	FROM
	
	(SELECT salary AS `sum_start` FROM salary WHERE bonus = 0 AND salary IS NOT NULL
	UNION
	SELECT salary * bonus_mult FROM salary WHERE bonus = 1
	UNION
	SELECT ps.quantity * m.price
	FROM purchase_sch ps
	JOIN medicaments m ON m.id = ps.drug_id
	
	WHERE MONTH(ps.procedure_date) = desired_month
	) AS expenses;

END$$
DELIMITER ;


CALL expenses(10);












/*
 З А М Е Т К И   aka нереализованные идеи (для автора)))))
 
1. Триггер на количество пациентов в палатах (?!?!)

(Селект в скобках) = 1 то есть True:

(SELECT
COUNT(*) <= (SELECT pers_count FROM rooms_info WHERE room_num = room) AS `не переполнена` 
FROM med_rooms
WHERE status = 1 AND DATE_ADD(date_of_status_change, INTERVAL (SELECT day_staying FROM patients
WHERE patient_id = id) DAY) > current_date() AND room = вот тут должен быть номер комнаты вставки) = 1


2. Цикл for на количество препаратов и с интервалом в два дня добавлять в лог процедур инъекции прописанных
препаратов (тип процедуры 87)

 */