-- Employees table
CREATE TABLE employees(
  emp_no INTEGER,
  emp_title_id VARCHAR(5),
  birth_date DATE,
  first_name VARCHAR,
  last_name VARCHAR,
  sex CHAR(1),
  hire_date DATE
);

SELECT *
FROM employees LIMIT 7;

SELECT COUNT(DISTINCT(emp_title_id)) FROM employees;
