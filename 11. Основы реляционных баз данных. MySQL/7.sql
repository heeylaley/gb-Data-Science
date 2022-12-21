-- 1. Составьте список пользователей users, которые осуществили хотя бы один заказ orders
-- в интернет магазине.

SELECT DISTINCT u.name 
FROM users u 
LEFT JOIN orders o
ON u.id = o.user_id 


-- 2. Выведите список товаров products и разделов catalogs, который соответствует товару.

SELECT
	p.product_id,
	p.product_name,
	p.value,
	c.name
FROM products p
JOIN
catalogs c
ON p.product_id = c.id


/* 3. (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов
cities (label, name). Поля from, to и label содержат английские названия городов,
поле name — русское. Выведите список рейсов flights с русскими названиями городов. */

SELECT
	f.id,
	f.depart,
	f.dest
FROM (SELECT
		f.id,
		f.depart,
		f.dest
	FROM flights f
	JOIN cities c
	ON f.dest = c.label) AS f
JOIN cities c
ON (f.depart = c.label)






