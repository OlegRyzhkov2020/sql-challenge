# SQL Homework - Employee Database: A Mystery in Two Parts

Data Science and Visualization Boot Camp (Northwestern University)

![GitHub last commit](https://img.shields.io/github/last-commit/OlegRyzhkov2020/api-challenge)
![GitHub top language](https://img.shields.io/github/languages/top/OlegRyzhkov2020/api-challenge)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![HitCount](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge.svg)](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge)
![GitHub watchers](https://img.shields.io/github/watchers/OlegRyzhkov2020/api-challenge?label=Watch&style=social)
![GitHub followers](https://img.shields.io/github/followers/OlegRyzhkov2020?label=Follow&style=social)

![presentation_slide](images/slide_question.png)

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

## Data exploration


## Data Visualization



## Contacts
[Find Me on
LinkedIn](https://www.linkedin.com/in/oleg-n-ryzhkov/)
