/* 1. Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека,
который больше всех общался с нашим пользователем. */

USE vk;

SELECT
    COUNT(*) as cnt,
    from_user_id,
    to_user_id as 'Кому',
    (SELECT firstname from users WHERE id = from_user_id) as 'ownName',
    (SELECT lastname from users WHERE id = from_user_id) as 'ownLastName'
FROM messages
WHERE to_user_id = 1
GROUP BY from_user_id
ORDER BY COUNT(*) DESC
LIMIT 1;



-- 2. Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.

SELECT count(*)
FROM likes
WHERE media_id IN (
	SELECT id 
	FROM media 
	WHERE user_id IN (
		SELECT user_id FROM profiles AS p
		WHERE  YEAR(CURDATE()) - YEAR(birthday) < 11
	)
);



-- 3. Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT 
	gender,
	count(*)
FROM (
	SELECT 
		user_id AS USER,
		(
			SELECT gender 
			FROM vk.profiles
			WHERE user_id = user
		) AS gender
	FROM likes
) AS dummy
GROUP BY gender;
