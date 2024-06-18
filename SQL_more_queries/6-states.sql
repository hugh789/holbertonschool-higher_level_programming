-- creates a database hbtn_0d_usa and table states
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table states already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);