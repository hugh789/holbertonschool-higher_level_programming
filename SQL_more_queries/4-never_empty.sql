-- creates a table id_not_null
-- id_not_null description:
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, your script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256)
);