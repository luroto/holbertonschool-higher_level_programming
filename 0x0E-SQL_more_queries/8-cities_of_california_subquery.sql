-- This script list all the ciites of California found in some database
-- states_id must be used for searching
SELECT `state_id`, `name` FROM cities
WHERE `state_id` =
  (SELECT `id` FROM states WHERE `name` = 'California')
ORDER BY cities.id ASC;
