-- This script creates a table on MySQL server
--  It will be created attending some criteria and only if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
