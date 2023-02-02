-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS holberton;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON holberton.* TO root@localhost;

USE holberton;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256),
    email VARCHAR(256),
    phone VARCHAR(16),
    ssn VARCHAR(16),
    password VARCHAR(256),
    ip VARCHAR(64),
    last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

LOAD DATA INFILE '/var/lib/mysql-files/user_data.csv'
INTO TABLE users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
