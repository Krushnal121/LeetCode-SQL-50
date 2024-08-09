SELECT x, y, z,
(CASE
WHEN (x+y+z)>GREATEST(x,y,z)*2 THEN 'Yes'
ELSE 'No'
END) AS triangle
FROM Triangle