-- This script lists all the genres that are not linked with any shows
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings LEFT JOIN tv_shows
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
