-- gets list of ALL show titles with genre ids (where available)
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
-- Imported the database dump from hbtn_0d_tvshows (provided/downloaded)

SELECT title, genre_id FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
ORDER BY title ASC, genre_id ASC;