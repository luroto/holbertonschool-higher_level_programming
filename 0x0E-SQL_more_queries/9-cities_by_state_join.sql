-- This script lists all cities contained in some database using some criteria
-- Only one SELECT statement
SELECT cities.id, cities.name, states.name FROM states, cities
ORDER BY cities.id DESC;
