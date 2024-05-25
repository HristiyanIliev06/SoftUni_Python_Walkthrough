/*SELECT p.id, p.name, p.description, p.start_date,
	CASE WHEN p.end_date IS NULL THEN p.start_date +  INTERVAL '5 month' 
	ELSE p.end_date
	END
FROM projects AS p;*/

UPDATE 
	projects
SET
	end_date = start_date +  INTERVAL '5 month'
WHERE
	end_date IS NULL
RETURNING *;




