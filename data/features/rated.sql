SELECT movie_id,
       CASE
           WHEN rated = "PG-13" THEN 1
           WHEN rated = "PG" THEN 2
           WHEN rated = "R" THEN 3
           WHEN rated = "NOT RATED" THEN 4
           WHEN rated = "G" THEN 5
           WHEN rated = "NC-17" THEN 6
           WHEN rated = "UNRATED" THEN 7
           WHEN rated = "TV-MA" THEN 8                               
           ELSE -1
       END
       AS rated
FROM movies
