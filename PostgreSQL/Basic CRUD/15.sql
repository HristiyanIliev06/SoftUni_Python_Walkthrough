CREATE TABLE company_chart
	AS SELECT e.first_name||' '||e.last_name AS full_name, e.job_title, e.department_id, e.manager_id
	FROM employees AS e;