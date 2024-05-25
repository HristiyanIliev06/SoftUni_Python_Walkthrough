SELECT e."id" AS id, e."first_name" || ' ' || e."middle_name" || ' ' || e."last_name" AS "full_name", e."hire_date"
	FROM employees as e
ORDER BY hire_date OFFSET 9;