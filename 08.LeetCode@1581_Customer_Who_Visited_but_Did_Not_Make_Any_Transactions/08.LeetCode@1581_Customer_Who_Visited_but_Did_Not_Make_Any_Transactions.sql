SELECT VISIT.customer_id, COUNT(VISIT.visit_id) AS count_no_trans
FROM Visits VISIT
LEFT JOIN Transactions TRAN ON
VISIT.visit_id=TRAN.visit_id
WHERE TRAN.transaction_id IS NULL
GROUP BY VISIT.customer_id;