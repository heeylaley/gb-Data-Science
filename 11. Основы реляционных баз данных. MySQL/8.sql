/* 1. Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите
человека, который больше всех общался с выбранным пользователем (написал ему сообщений).
*/

SELECT 
	from_user_id,
	CONCAT(u.firstname, ' ', u.lastname) AS name,
	COUNT(*) as cnt
FROM messages m
JOIN users u ON u.id = m.from_user_id
JOIN friend_requests fr ON (fr.initiator_user_id=m.to_user_id AND
							fr.target_user_id=m.from_user_id) OR
                            (fr.target_user_id=m.to_user_id AND
							fr.initiator_user_id=m.from_user_id)
WHERE m.to_user_id = 1
GROUP BY m.from_user_id
ORDER BY cnt DESC
LIMIT 1;


-- 2. Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.
SELECT COUNT(*)
FROM likes l
JOIN media m ON l.media_id = m.id
JOIN profiles p ON p.user_id = m.user_id
WHERE YEAR(NOW()) - YEAR(birthday) < 11;


-- 3. Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT CASE (gender)
	WHEN 'm' THEN 'мужчин'
	WHEN 'f' THEN 'женщин'
	END AS 'Кого больше', COUNT(*) AS 'лайков'
FROM profiles p 
JOIN likes l 
WHERE l.user_id = p.user_id
GROUP BY gender 
LIMIT 1