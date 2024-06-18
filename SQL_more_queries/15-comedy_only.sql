-- lists all Comedy shows in database
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement

SELECT title 
FROM tv_genres g 
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id 
INNER JOIN tv_shows s ON sg.show_id = s.id 
WHERE name = "Comedy"
ORDER BY title ASC;