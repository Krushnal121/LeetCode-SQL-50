SELECT* FROM Cinema
WHERE description !="boring"
AND ID%2 = 1
ORDER BY rating DESC