-- Creating Schema for EmployeesSQL Case

-- Title table
DROP TABLE IF EXISTS title
CREATE TABLE title(
  title_id VARCHAR(5) NOT NULL PRIMARY KEY,
  title VARCHAR(20) NOT NULL
);
SELECT * FROM title LIMIT 10;
	
-- Employees table
DROP TABLE IF EXISTS employees
CREATE TABLE employees(
  emp_no INTEGER PRIMARY KEY,
  emp_title_id VARCHAR(5) REFERENCES title (title_id),
  birth_date DATE,
  first_name VARCHAR,
  last_name VARCHAR,
  sex CHAR(1),
  hire_date DATE
);
SELECT COUNT(DISTINCT(emp_title_id)) FROM employees;
SELECT * FROM employees LIMIT 20;

-- Salary table
DROP TABLE IF EXISTS salary
CREATE TABLE salary(
  emp_no INTEGER PRIMARY KEY REFERENCES employees (emp_no),
  salary INTEGER NOT NULL
);
SELECT * FROM salary LIMIT 10;

-- Departments table
DROP TABLE departments
CREATE TABLE departments(
  dept_no VARCHAR(5) PRIMARY KEY,
  dept_name VARCHAR(20) NOT NULL
);
SELECT * FROM departments LIMIT 10;

-- Department_managers table
DROP TABLE IF EXISTS dept_managers
CREATE TABLE dept_managers(
  dept_no VARCHAR(5) REFERENCES departments (dept_no),
  emp_no INTEGER REFERENCES employees (emp_no)
);
SELECT * FROM dept_managers LIMIT 10;

-- Department_employees table
DROP TABLE IF EXISTS dept_employees
CREATE TABLE dept_employees(
  emp_no INTEGER REFERENCES employees (emp_no),
  dept_no VARCHAR(5) REFERENCES departments (dept_no)
);
SELECT * FROM dept_employees LIMIT 10;
