SELECT DISTINCT A.num AS ConsecutiveNums
FROM Logs A INNER JOIN
Logs B ON
A.id+1=B.id AND A.num=B.num
INNER JOIN
Logs C ON
B.id+1=C.id AND B.num=C.num