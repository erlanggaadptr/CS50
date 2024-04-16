SELECT people.name FROM people
JOIN stars AS stars1 ON people.id = stars1.person_id
JOIN stars AS stars2 ON stars1.movie_id = stars2.movie_id
WHERE stars2.person_id = (SELECT id FROM people WHERE name = "Kevin Bacon" AND birth = 1958)
AND people.name != "Kevin Bacon";
