-- This script list all shows contained in the databes
SELECT DISTINCT tv_shows.title,  tv_show_genres.genre_id FROM tv_shows, tv_show_genres
LEFT JOIN tv_
WHERE tv_shows.id = tv_show_genres.show_id OR tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
