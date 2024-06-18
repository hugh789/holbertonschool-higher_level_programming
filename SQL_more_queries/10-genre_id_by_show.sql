-- gets list of show titles with their genre ids
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Imported the database dump from hbtn_0d_tvshows (provided/downloaded)
-- You can use only one SELECT statement

SELECT title, genre_id FROM tv_shows s
INNER JOIN tv_show_genres sg ON s.id = sg.show_id
ORDER BY title ASC, genre_id ASC;