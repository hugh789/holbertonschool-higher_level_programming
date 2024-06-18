-- selects all the cities of California from the cities table
-- Results must be sorted in ascending order by cities.id
-- JOIN keyword can't be used
--  database name will be passed as an argument of the mysql command

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");