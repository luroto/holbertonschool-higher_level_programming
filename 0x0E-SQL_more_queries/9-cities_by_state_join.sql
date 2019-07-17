-- This script lists all cities contained in some database using some criteria
-- Only one SELECT statement
SELECT cities.*, states.* FROM cities, states
WHERE cities.id = states.id
ORDER BY cities.id DESC;
