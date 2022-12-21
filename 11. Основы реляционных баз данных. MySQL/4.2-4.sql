-- 2. Написать скрипт, возвращающий список имен (только firstname)
-- пользователей без повторений в алфавитном порядке.

SELECT firstname
FROM users
GROUP BY firstname
ORDER BY firstname;


-- 3. Первые пять пользователей пометить как удаленные.

-- 3.1
UPDATE users
SET is_deleted = b'1'
WHERE id<6;

-- 3.2
UPDATE users
SET is_deleted = b'1'
ORDER by id
LIMIT 5;


-- 4. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней).

DELETE FROM messages
WHERE created_at < NOW();