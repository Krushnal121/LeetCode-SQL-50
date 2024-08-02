SELECT A.product_id, A.first_year, B.quantity, B.price
FROM
    (SELECT DISTINCT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id) A
INNER JOIN Sales B
ON A.product_id=B.product_id AND A.first_year=B.year