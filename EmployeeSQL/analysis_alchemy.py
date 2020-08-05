import sqlalchemy as sqlalchemy_package
from sqlalchemy.sql import select
from sqlalchemy import create_engine, desc, func, case, cast, and_
from sqlalchemy import Table, MetaData, Column, Integer, Float, String, ForeignKey
import config_psql as creds
import pandas as pd

# Set up a connection to the postgres server
DATABASE_URL = f"postgres://{creds.PGUSER}:{creds.PGPASSWORD}@{creds.PGHOST}:5432/{creds.PGDATABASE}"
engine = sqlalchemy_package.create_engine(DATABASE_URL)
connection = engine.connect()

# Build Tables Representation within SQLAlchemy
metadata = MetaData(bind=None)
emp = Table('employees', metadata, autoload = True, autoload_with = engine)
sal = Table('salary', metadata, autoload = True, autoload_with = engine)
dep = Table('departments', metadata, autoload = True, autoload_with = engine)
dep_emp = Table('dept_employees', metadata, autoload = True, autoload_with = engine)

# Execute the query to retrieve the selected data returned into results
emp_data = select([emp]).where(emp.columns.emp_no == 499942)
results = connection.execute(emp_data).fetchall()
# Loop over the results and print the selected data
print('\nQuery output for the employee with a particular number:')
for result in results:
    print(result.emp_no, result.first_name, result.last_name,
            result.sex, result.hire_date)

# Execute the query to retrieve the selected data returned into results
stmt = select([
    emp.columns.sex.label('gender'),
    func.avg(sal.columns.salary).label('avg_salary')
    ])
stmt_join = stmt.select_from(
    emp.join(sal, emp.columns.emp_no == sal.columns.emp_no))
stmt_grouped = stmt_join.group_by(emp.columns.sex)
results = connection.execute(stmt_grouped).fetchall()
# Store Table in DataFrame
print('\nQuery output for the average salary by gender stored to DataFrame:')
emp_df = pd.DataFrame(results)
emp_df.columns = results[0].keys()
print(emp_df, '\n')

# Execute the query to retrieve the selected data returned into results
stmt = select([
    dep.columns.dept_name,
    func.avg(sal.columns.salary).label('avg_salary'),
        (func.sum(
            case([
                (emp.columns.sex == 'M', 1)
            ], else_=0)) /
         cast(func.count(emp.columns.sex), Float) * 100).label('percent_male')
    ])
stmt_join = stmt.select_from(
    emp.join(dep_emp.join(dep, dep_emp.columns.dept_no == dep.columns.dept_no),
     emp.columns.emp_no == dep_emp.columns.emp_no).join(sal, emp.columns.emp_no == sal.columns.emp_no))
stmt_grouped = stmt_join.group_by(dep.columns.dept_name).order_by(desc('percent_male'))
results = connection.execute(stmt_grouped).fetchall()
gender_df = pd.DataFrame(results)
gender_df.columns = results[0].keys()
print('Query output for statistics by department stored to DataFrame:')
print(gender_df, '\n')
