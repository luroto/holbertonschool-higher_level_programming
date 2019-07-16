-- This script creates another database and some of its fields and insert data
-- I'll try step by step
CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR (256), score INT);
INSERT INTO second_table (`id`, `name`, `score`)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
