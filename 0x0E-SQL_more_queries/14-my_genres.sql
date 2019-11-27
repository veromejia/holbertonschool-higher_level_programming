-- use the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Results must be sorted in ascending order by the genre name
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
