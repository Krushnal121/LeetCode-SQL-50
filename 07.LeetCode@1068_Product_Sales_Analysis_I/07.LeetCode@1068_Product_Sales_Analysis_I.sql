SELECT PR.product_name,SL.year,SL.price FROM Sales SL
LEFT JOIN Product PR ON
SL.product_id=PR.product_id;