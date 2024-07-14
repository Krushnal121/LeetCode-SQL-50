SELECT UNI.unique_id, Employees.name FROM Employees
LEFT JOIN EmployeeUNI UNI
ON UNI.id = Employees.id;