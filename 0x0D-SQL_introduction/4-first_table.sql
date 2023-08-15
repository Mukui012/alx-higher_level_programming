-- script that creates table in current database
-- script won't fail if the table already exists

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
