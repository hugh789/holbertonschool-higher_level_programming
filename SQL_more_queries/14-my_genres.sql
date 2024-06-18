-- List all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement

SELECT DISTINCT (name) 
FROM tv_shows s 
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id 
LEFT JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = "Dexter"
ORDER BY name ASC;