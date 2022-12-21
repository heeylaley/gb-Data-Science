--   “Транзакции, переменные, представления”

/* 1. В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы
данных. Переместите запись id = 1 из таблицы shop.users в таблицу sample.users.
Используйте транзакции. */

START TRANSACTION;
INSERT INTO sample.users (SELECT * FROM shop.users WHERE shop.users.id = 1);
DELETE FROM shop.users WHERE id=1 LIMIT 1;
COMMIT;



/* 2. Создайте представление, которое выводит название name товарной позиции из
таблицы products и соответствующее название каталога name из таблицы catalogs.*/

CREATE OR REPLACE VIEW prod_desc(prod_id, prod_name, cat_name) AS
SELECT p.id AS prod_id, p.name, cat.name
FROM products AS p
LEFT JOIN catalogs AS cat 
ON p.catalog_id = cat.id;


/* 4. Пусть имеется любая таблица с календарным полем created_at.
Создайте запрос, который удаляет устаревшие записи из таблицы,
оставляя только 5 самых свежих записей. */

DROP TABLE IF EXISTS timetime;
CREATE TEMPORARY TABLE timetime (
	name VARCHAR(30),
	rtime DATE);

INSERT into timetime VALUES
	('Regina', '2000-12-08'),
	('Renata', '2000-10-08'),
	('Victoria', '2000-12-19'),
	('Felix', '2000-12-03'),
	('Victor', '2000-11-04'),
	('Reginald', '2000-10-16'),
	('Kevin', '2000-11-20'),
	('James', '2000-11-15');


PREPARE del_el from "DELETE FROM timetime ORDER BY rtime LIMIT ?";
SET @ROWS = (SELECT COUNT(*) - 5 FROM timetime);
EXECUTE del_el USING @ROWS;


SELECT * FROM timetime
ORDER BY rtime DESC





--  “Администрирование MySQL”

/* 1. Создайте двух пользователей которые имеют доступ к базе данных shop.
Первому пользователю shop_read должны быть доступны только запросы на
чтение данных, второму пользователю shop — любые операции в пределах
базы данных shop. */

CREATE USER 'shop_read';
GRANT SELECT ON shop.* TO 'shop_read'; -- чтение

CREATE USER 'shop';
GRANT ALL ON shop.* TO 'shop'; -- любые операции



/* 2. Пусть имеется таблица accounts содержащая три столбца id, name,
password, содержащие первичный ключ, имя пользователя и его пароль.
Создайте представление username таблицы accounts, предоставляющий доступ
к столбца id и name. Создайте пользователя user_read, который бы не имел
доступа к таблице accounts, однако, мог бы извлекать записи из представления
username. */

CREATE OR REPLACE VIEW username AS
SELECT a.id, a.name FROM accounts a;

SELECT * FROM username;

CREATE USER 'user_read';
GRANT SELECT ON shop.username TO 'user_read';




--  “Хранимые процедуры и функции, триггеры"

/* 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в
зависимости от текущего времени суток. С 6:00 до 12:00 функция должна возвращать
фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день",
с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи". */

DROP PROCEDURE IF EXISTS hello;

DELIMITER //
CREATE FUNCTION hello ()
RETURNS TINYTEXT NOT DETERMINISTIC
BEGIN
	DECLARE hour INT;
    SET hour = HOUR(NOW());
	CASE
		WHEN hour BETWEEN 0 AND 5 THEN
			RETURN 'Доброй ночи';
		WHEN hour BETWEEN 6 AND 11 THEN
			RETURN 'Доброе утро';
		WHEN hour BETWEEN 12 AND 17 THEN
			RETURN 'Добрый день';
		WHEN hour BETWEEN 18 AND 23 THEN
			RETURN 'Добрый вечер';
	END CASE;
END //
DELIMITER ;


call hello();



/* 2. В таблице products есть два текстовых поля: name с названием товара и description
с его описанием. Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба
поля принимают неопределенное значение NULL неприемлема. Используя триггеры, добейтесь
того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям
NULL-значение необходимо отменить операцию. */

ALTER TABLE products
ADD CHECK (name AND description IS NOT NULL);



/* 3. (по желанию) Напишите хранимую функцию для вычисления произвольного числа
Фибоначчи. Числами Фибоначчи называется последовательность в которой число равно
сумме двух предыдущих чисел. Вызов функции FIBONACCI(10) должен возвращать число 55.*/

DROP TABLE IF EXISTS fibonac;
CREATE TEMPORARY TABLE fibonac (
	id SMALLINT,
	num INT);

INSERT INTO fibonac VALUES (0, 0);


DROP PROCEDURE IF EXISTS fibonacci;

DELIMITER //
CREATE PROCEDURE fibonacci
(a SMALLINT)
BEGIN
	DECLARE i INT DEFAULT 1;
	DECLARE j INT DEFAULT 1;
	WHILE i < a + 1 DO
		INSERT INTO fibonac VALUES(i, j);
		SET j = j + (SELECT num FROM fibonac WHERE id = i - 1);
		SET i = i + 1;
	END WHILE;
END //
DELIMITER ;


CALL fibonacci(10);
	

SELECT * FROM fibonac;

