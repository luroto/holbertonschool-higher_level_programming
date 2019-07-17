-- This script list all the ciites of California found in some database
-- states_id must be used for searching
SELECT `state_id`, `name` FROM cities
WHERE `id` =
  (SELECT `id` FROM states WHERE `name` = 'California')
ORDER BY cities.id;
