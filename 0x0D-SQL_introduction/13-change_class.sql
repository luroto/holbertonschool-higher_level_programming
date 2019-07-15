-- This script deletes rows from second_table given some criteria
-- Score below 5 will be removed
DELETE FROM second_table
WHERE `score` <= 5;
