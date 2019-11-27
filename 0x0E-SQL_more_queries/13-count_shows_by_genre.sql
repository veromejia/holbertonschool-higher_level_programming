-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Results must be sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, count(*) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
