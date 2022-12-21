/* 1. Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users,
catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы,
идентификатор первичного ключа и содержимое поля name. */

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	created_at DATETIME,
	tablename varchar(100) NULL,
	id BIGINT UNSIGNED NULL,
	name varchar(100) NULL)
ENGINE=ARCHIVE;


DROP TRIGGER IF EXISTS users_logs

delimiter //
CREATE TRIGGER users_logs AFTER INSERT ON users 
FOR EACH ROW
BEGIN 
	INSERT INTO logs (created_at, tablename, id, name)
	VALUES(NOW(), 'users', NEW.id, NEW.name);
END //
delimiter ;


DROP TRIGGER IF EXISTS catalogs_logs

delimiter //
CREATE TRIGGER catalogs_logs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN 
	INSERT INTO logs (created_at, tablename, id, name)
	VALUES(NOW(), 'catalogs', NEW.id, NEW.name);
END //
delimiter ;


DROP TRIGGER IF EXISTS products

delimiter //
CREATE TRIGGER products_logs AFTER INSERT ON products
FOR EACH ROW
BEGIN 
	INSERT INTO shop.logs (created_at, tablename, id, name)
	VALUES(NOW(), ' products', NEW.id, NEW.name);
END //
delimiter ;




-- 2. Создайте SQL-запрос, который помещает в таблицу users миллион записей.

CREATE TABLE samples (
	id SERIAL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'имя покупателя',
    bithday_at DATE COMMENT 'дата рождения',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);

INSERT INTO samples(name, birthday_at) VALUES -- 10 записей
	('Валерия', '1990-10-10'),
    ('Максим', '1990-11-11'),
    ('Елена', '1990-12-12'),
    ('Екатерина', '1990-01-01'),
    ('Юрий', '1991-02-09'),
    ('Аркадий', '1999-03-04'),
    ('Ярослав', '1997-09-08'),
    ('Мирослава', '1997-08-08'),
    ('Сергей', '1998-08-10'),
    ('Анна', '1999-02-04');

INSERT INTO
	users(name, birthday_at)
SELECT fst.name, fst.birthday_at
FROM
	samples AS fst,
    samples AS snd,
    samples AS trd
    samples AS fth,
    samples AS fif,
    samples AS sth;  -- 10 ^ 6 = 1000000 записей
