import sqlalchemy as sqlalchemy_package
from sqlalchemy.sql import select
from sqlalchemy import create_engine, desc, func, and_
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
import config_psql as creds
import pandas as pd

# Set up a connection to the postgres server
DATABASE_URL = f"postgres://{creds.PGUSER}:{creds.PGPASSWORD}@{creds.PGHOST}:5432/{creds.PGDATABASE}"
engine = sqlalchemy_package.create_engine(DATABASE_URL)
connection = engine.connect()
# employees = pd.read_sql('employees', engine)
# print(employees.head())

# Build Tables Representation within SQLAlchemy
metadata = MetaData(bind=None)
emp = Table('employees', metadata, autoload = True, autoload_with = engine)
sal = Table('salary', metadata, autoload = True, autoload_with = engine)

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
print('\nQuery output for the average salary by gender and stored to DataFrame:')
emp_df = pd.DataFrame(results)
emp_df.columns = results[0].keys()
print(emp_df)
