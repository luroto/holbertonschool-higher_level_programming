-- This script lists all records of second_table given some criteria
-- Rows lacking name field will be excluded
SELECT `score`, `name` FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
