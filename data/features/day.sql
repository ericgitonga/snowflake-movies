SELECT movie_id,
       CASE
           WHEN day = "Monday" THEN 1
           WHEN day = "Tuesday" THEN 2
           WHEN day = "Wednesday" THEN 3
           WHEN day = "Thursday" THEN 4
           WHEN day = "Friday" THEN 5
           WHEN day = "Saturday" THEN 6
           WHEN day = "Sunday" THEN 7                    
           ELSE -1
       END
       AS day
FROM movies
