WITH rec as (
    SELECT requester_id id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id id FROM RequestAccepted
)
SELECT id, count(*) num
FROM rec
GROUP BY 1
ORDER BY 2 DESC LIMIT 1