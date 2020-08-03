# SQL Homework - Employee Database: A Mystery in Two Parts

Data Science and Visualization Boot Camp (Northwestern University)

![GitHub last commit](https://img.shields.io/github/last-commit/OlegRyzhkov2020/api-challenge)
![GitHub top language](https://img.shields.io/github/languages/top/OlegRyzhkov2020/api-challenge)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![HitCount](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge.svg)](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge)
![GitHub watchers](https://img.shields.io/github/watchers/OlegRyzhkov2020/api-challenge?label=Watch&style=social)
![GitHub followers](https://img.shields.io/github/followers/OlegRyzhkov2020?label=Follow&style=social)

## Case ERD

![presentation_slide](images/employees_erd.png)

## Creating schema

```sql
CREATE TABLE employees(
 emp_no INTEGER PRIMARY KEY,
 emp_title_id VARCHAR(5) REFERENCES title (title_id),
 birth_date DATE,
 first_name VARCHAR,
 last_name VARCHAR,
 sex CHAR(1),
 hire_date DATE
);
```

## Data reading and exploration

```python
# Set up a connection to the postgres server.
conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
+" password="+ creds.PGPASSWORD
conn=psycopg2.connect(conn_string)
print(f"PostgreSQL Database {creds.PGDATABASE} is connected!")

# Create a cursor object
cursor = conn.cursor()
```
![presentation_slide](images/exploration.png)

## Data Visualization

![presentation_slide](images/visualization.png)


## Contacts
[Find Me on
LinkedIn](https://www.linkedin.com/in/oleg-n-ryzhkov/)
