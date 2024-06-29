-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.

SELECT cities.name
FROM cities
WHERE cities.states_id = (
    SELECT state.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;