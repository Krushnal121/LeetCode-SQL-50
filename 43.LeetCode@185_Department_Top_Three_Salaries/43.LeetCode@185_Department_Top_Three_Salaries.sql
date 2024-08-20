SELECT B.name AS Department,
A.name AS Employee,
A.salary AS salary
FROM Employee A JOIN Department B
ON A.departmentId=B.ID
WHERE(
        SELECT COUNT(DISTINCT salary)
        FROM Employee A2
        WHERE A2.departmentId = A.departmentId AND A2.salary >= A.salary
) <= 3
ORDER BY Department, Salary DESC