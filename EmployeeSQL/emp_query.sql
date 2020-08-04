--Data Analysis

--Schema Names List
select schema_name
from information_schema.schemata;

--Employees Salary List
SELECT e.emp_no, e.first_name, e.last_name, e.sex, s.salary
FROM employees AS e
INNER JOIN salary AS s USING (emp_no);

--Employees Hired in 1986 List
SELECT e.first_name, e.last_name, e.hire_date
FROM employees AS e
WHERE EXTRACT(YEAR FROM e.hire_date) = 1986;

--Employees Departments Managers List
SELECT dm.dept_no, d.dept_name, e.emp_no, e.first_name, e.last_name
FROM dept_managers AS dm
INNER JOIN departments AS d USING (dept_no)
INNER JOIN employees AS e USING (emp_no);

--Employees & Department names List
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
FROM employees AS e
INNER JOIN dept_employees USING (emp_no)
INNER JOIN departments AS d USING (dept_no) ORDER BY dept_no;

--Employees with First Name Hercules and Last Name starts B List
SELECT e.first_name, e.last_name, e.sex
FROM employees AS e
WHERE e.first_name = 'Hercules' AND e.last_name LIKE 'B%' ORDER BY e.last_name;

--Employees Sales Department names List
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
FROM employees AS e
INNER JOIN dept_employees USING (emp_no)
INNER JOIN departments AS d USING (dept_no) 
WHERE d.dept_name = 'Sales' ORDER BY e.emp_no;

--Employees Sales and Development Department names List
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
FROM employees AS e
INNER JOIN dept_employees USING (emp_no)
INNER JOIN departments AS d USING (dept_no) 
WHERE d.dept_name = 'Sales' or d.dept_name = 'Development' ORDER BY e.emp_no;

--Employees share Last Name List
SELECT DISTINCT last_name, COUNT(last_name) AS frequency_count
FROM employees
GROUP BY last_name ORDER BY frequency_count DESC LIMIT 20;

--Employees Number 499942 (April 1 - Foolsday)
SELECT e.first_name, e.last_name, e.hire_date
FROM employees AS e
WHERE e.emp_no = 499942;
