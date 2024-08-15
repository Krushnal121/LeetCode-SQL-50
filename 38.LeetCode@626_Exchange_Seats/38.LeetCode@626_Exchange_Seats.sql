SELECT A.id,
       CASE
           WHEN A.id % 2 = 0 THEN (SELECT B.student FROM Seat B WHERE B.id = A.id - 1)
           WHEN A.id % 2 = 1 THEN
               COALESCE(
                   (SELECT B.student FROM Seat B WHERE B.id = A.id + 1),
                   (SELECT B.student FROM Seat B WHERE B.id = A.id)
               )
       END AS student
FROM Seat A
ORDER BY A.id;