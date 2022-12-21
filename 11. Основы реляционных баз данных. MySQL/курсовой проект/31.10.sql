-- 31.10. Выполняем задания вручную




-- Вложенные запросы

-- 1. Смотрим пациентов, которые в нашем отделении на 31 октября
SELECT

id,
name AS 'ФИО',
(SELECT disease_name FROM disease_vocab WHERE id = diagnosis) AS `Диагноз`,
concomitant AS 'Сопутствующие заболевания',
(SELECT room FROM med_rooms WHERE patient_id = id AND status = 1) AS `Палата`,
(SELECT date_of_status_change FROM med_rooms WHERE patient_id = id AND status = 1) AS `Поступил/а`,
day_staying AS `Дней пребывания`

FROM patients
WHERE DATE_ADD(arr_date, INTERVAL day_staying DAY) >= '2022-10-31'
ORDER BY `Палата`;





-- 2. Посмотрим на разброс заболеваний
SELECT

(SELECT disease_name FROM disease_vocab WHERE id = diagnosis) AS `Диагноз`,
COUNT(*) AS `Количество`

FROM patients
WHERE DATE_ADD(arr_date, INTERVAL day_staying DAY) >= '2022-10-31'
GROUP BY `Диагноз`;





-- 3. Проверяем, выписывается ли кто-нибудь 31 октября и нужен ли им больничный лист
SELECT

id,
name AS 'ФИО',
(SELECT disease_name FROM disease_vocab WHERE id = diagnosis) AS `Диагноз`,
concomitant AS 'Сопутствующие заболевания',
(SELECT room FROM med_rooms WHERE patient_id = id AND status = 1) AS `Палата`,
(SELECT date_of_status_change FROM med_rooms WHERE patient_id = id AND status = 1) AS `Поступил/а`,
day_staying AS `Дней пребывания`,
sickleave AS 'Больничный лист'

FROM patients
WHERE DATE_ADD(arr_date, INTERVAL day_staying DAY) = '2022-10-31';



--  4. Проверим, сколько пациентов можно записать 1.11
SELECT SUM(`свободных мест`) AS 'свободных мест'
FROM

(SELECT

(SELECT pers_count FROM rooms_info WHERE room_num = room) - COUNT(*) AS `свободных мест`

FROM med_rooms
WHERE status = 1 AND
	DATE_ADD(date_of_status_change, INTERVAL (SELECT day_staying FROM patients
	WHERE patient_id = id) DAY) > '2022-10-31'
GROUP BY room

) AS vacant;




--  5. Проверим, всем ли пациентам взяли кровь на следующий день после поступления
SELECT
(SELECT COUNT(*) FROM procedure_sch WHERE procedure_type = 11) = (SELECT COUNT(id) FROM patients)
AS 'проверка';





-- JOIN'ы



/* 6. Кровь могут брать как врачи, так и медработники. А гистологию кожи (код процедуры 232) могут
 * брать ТОЛЬКО врачи. Также гистологию должен брать именно лечащий врач. Посмотрим, соблюдаются ли эти
 * требования по равенству id лечащего врача из patients и executor из procedure_schedule
 */

SELECT

ps.procedure_type AS 'код процедуры',
ps.patient_id AS 'пациент',
ps.procedure_date AS 'дата взятия крови',
ps.executor AS `гистологию выполнил`,
p.doctor_id AS `id лечащего врача`,
s.cat = 1 AS 'выполнил врач',													-- ожидаем выход 1 = TRUE
(SELECT `гистологию выполнил` = `id лечащего врача`) AS 'врач один и тот же'	-- также ожидаем 1

FROM procedure_sch ps
JOIN patients p ON p.id = ps.patient_id
JOIN staff s ON s.id = executor 
WHERE procedure_type = 232
ORDER BY patient_id;




--  7. Посчитаем затраты, складывающиеся из закупок и зп

SELECT SUM(`sum_start`) AS 'суммарные затраты на октябрь'
FROM

(SELECT salary AS `sum_start` FROM salary WHERE bonus = 0 AND salary IS NOT NULL
UNION
SELECT salary * bonus_mult FROM salary WHERE bonus = 1
UNION
SELECT ps.quantity * m.price
FROM purchase_sch ps
JOIN medicaments m ON m.id = ps.drug_id

) AS expenses;


