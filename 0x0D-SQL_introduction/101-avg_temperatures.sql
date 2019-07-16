-- This script imports a table into a database and computes an average
-- Trying different options
SELECT `city`, AVG(`value`) AS avg_temp FROM temperatures
GROUP BY `city`
ORDER BY avg_temp DESC;
