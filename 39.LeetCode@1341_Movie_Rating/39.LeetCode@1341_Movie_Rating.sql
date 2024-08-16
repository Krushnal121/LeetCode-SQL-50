WITH modrating AS(
    SELECT *
    FROM MovieRating
    WHERE created_at>='2020-02-01' AND created_at<='2020-02-29'
)

SELECT * FROM (
    SELECT B.name AS results
    FROM MovieRating A
    JOIN Users B
    ON A.user_id = B.user_id
    GROUP BY A.user_id
    ORDER BY -(COUNT(movie_id)), B.name LIMIT 1
) AS results

UNION ALL

SELECT * FROM (
    SELECT B.title AS results
    FROM modrating A
    JOIN Movies B
    ON A.movie_id=B.movie_id
    GROUP BY A.movie_id
    ORDER BY -(SUM(rating)/COUNT(rating)), B.title LIMIT 1
) AS results