-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.

SELECT cities.name
FROM cities
WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;