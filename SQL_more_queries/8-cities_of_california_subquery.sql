-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.

SELECT name, id
FROM cities
WHERE state_id IN
(
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;