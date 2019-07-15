-- This script lists the number of records with the same score
-- It'll display the score and the number of records
SELECT `score`, COUNT(*) AS number
FROM second_table
GROUP BY `score` DESC;
