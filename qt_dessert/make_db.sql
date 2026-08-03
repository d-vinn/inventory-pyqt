CREATE DATABASE desertdb;

USE desertdb;

CREATE TABLE IF NOT EXISTS products (
  name VARCHAR(50) not null,
  price VARCHAR(50) not null,
  count INT not null
);

create table if not exists users(
	id varchar(50) not null,
    pw varchar(50) not null
);

INSERT INTO users (username, password) VALUES ('dabin', 'dabin11')
ON DUPLICATE KEY UPDATE password=VALUES(password);

insert into products (name, price, count) values (
('아메리카노', '3500', 3), ('라떼', '4000', 3), ('과일산도', '8000', 3), ('마카롱', '3000', 3), ('딸기 조각케이크', '7500', 3), ('에그타르트', '3000', 3));