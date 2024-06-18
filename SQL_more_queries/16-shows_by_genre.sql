-- list all shows and their linked genres
-- Display NULL in the genre column if a show doesn’t have a genre 
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement


SELECT title, name 
FROM tv_shows s 
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id 
LEFT JOIN tv_genres g ON sg.genre_id = g.id 
ORDER BY s.title ASC, name ASC;