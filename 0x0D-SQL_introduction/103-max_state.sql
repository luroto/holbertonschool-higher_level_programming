-- This script prints the top 3 cities with the highest temperature in some months
-- Trying again
SELECT `state`, MAX(`value`) AS max_temp FROM temperatures
GROUP BY `state`;
