SELECT A.person_name
FROM Queue A JOIN
Queue B ON
A.turn>=B.turn
GROUP BY A.turn
HAVING SUM(B.weight)<=1000
ORDER BY SUM(B.weight) DESC
LIMIT 1