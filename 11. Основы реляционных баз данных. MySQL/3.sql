-- Написать cкрипт, добавляющий в БД vk, которую создали на 3 вебинаре, 3-4 новые таблицы
-- (с перечнем полей, указанием индексов и внешних ключей).
-- (по желанию: организовать все связи 1-1, 1-М, М-М)

DROP TABLE IF EXISTS online_status;
CREATE TABLE online_status(
	active_user_id BIGINT UNSIGNED NOT NULL,
	status_online_user ENUM('Online', 'MobileOnline', 'Offline'),
	update_time DATETIME ON UPDATE CURRENT_TIMESTAMP,

	FOREIGN KEY (active_user_id) REFERENCES users(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT,
	INDEX (status_online_user),
	INDEX (update_time)

) COMMENT 'таблица активности пользователя';


DROP TABLE IF EXISTS apps;
CREATE TABLE apps(
	id SERIAL,
	name VARCHAR(150),
	is_free ENUM('free', 'paid'),
	admin_user_id BIGINT UNSIGNED NOT NULL,
	INDEX apps_name_idx(name),
	FOREIGN KEY (admin_user_id) references users(id)
);

DROP TABLE IF EXISTS users_apps;
CREATE TABLE users_apps(
	user_id BIGINT UNSIGNED NOT NULL,
	apps_id BIGINT UNSIGNED NOT NULL,

	PRIMARY KEY (user_id, apps_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (apps_id) REFERENCES apps(id)
);


DROP TABLE IF EXISTS goods_categories;
CREATE TABLE goods_categories (
	category_id SERIAL PRIMARY KEY,
	category_name VARCHAR(255) UNIQUE,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

) COMMENT 'Таблица категорий товаров';

DROP TABLE IF EXISTS goods_description;
CREATE TABLE goods_description (
	goods_id SERIAL PRIMARY KEY,
	goods_name VARCHAR(255),
	goods_photo VARCHAR(255) DEFAULT NULL,
	goods_description TEXT,
	goods_price DECIMAL(10,2),
	goods_category BIGINT UNSIGNED NOT NULL,
	user_posted_id BIGINT UNSIGNED NOT NULL,


    INDEX goods_category_idx(goods_category),

    FOREIGN KEY fk_goods_category(goods_category) REFERENCES goods_categories(category_id),
    FOREIGN KEY (user_posted_id) REFERENCES users(id)


) COMMENT 'Таблица с описанием товара';
