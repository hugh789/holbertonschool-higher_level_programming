-- selects all the cities of California from the cities table
-- The result should be sorted in ascending order by cities.id
-- You can use only one SELECT statement

SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id;