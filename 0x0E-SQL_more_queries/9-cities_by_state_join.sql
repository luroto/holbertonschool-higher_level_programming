-- This script lists all cities contained in some database using some criteria
-- Only one SELECT statement
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.id = states.id
ORDER BY cities.id DESC;
