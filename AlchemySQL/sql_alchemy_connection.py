import sqlalchemy as db
from sqlalchemy.sql import select
from sqlalchemy import create_engine, desc, func, and_
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
import config_psql as creds
import pandas as pd

DATABASE_URL = f"postgres://{creds.PGUSER}:{creds.PGPASSWORD}@{creds.PGHOST}:5432/{creds.PGDATABASE}"
engine = db.create_engine(DATABASE_URL)
connection = engine.connect()

stmt = db.select([employees.columns.emp_no, employees.columns.first_name])
# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchmany(10)

# Loop over the results and print the selected data
for result in results:
    print(result.emp_no, result.first_name, result.last_name)
