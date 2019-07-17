-- This script create a given table
-- Its fields will be id and name and id must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
