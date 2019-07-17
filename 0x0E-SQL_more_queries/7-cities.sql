-- This script creates a database and a table if it doesn't exist
-- This table will use a foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT, state_id INT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id) );
