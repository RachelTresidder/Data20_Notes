import sqlalchemy
# import pyodbc
import pandas as pd

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

# creating a connection
connection = engine.connect()
# wont print anything, but the connection will have been made

# once we have a connection open, we can execute multiple different sql queries - whether that is just selecting data
# or actually creating databases and tables

# execute queries
results = engine.execute('SELECT * FROM Products;')
print(results)
#    this will return an object we will need to access


# retrieve one row at a time from your result
first_row = results.fetchone()
print(first_row)
#   printed row 1 for 'Chai'
#       but no column labels to make the data understandable - RESEARCH THIS!


# retrieve multiple rows at a time
many_rows = results.fetchmany(10)
print(many_rows)
#   in this code we need to specify how many we want to retrieve in the ()
#       returned 10 rows as lists one after another in a long line
# appears to have returned from row 2 to row 11


# retrieving everything
all_results = results.fetchall()
print(all_results)
#   every row was returned, each as a list, in a very long line
# returned from row 12 to end

# at first, grabs the data but doesnt store everything properly
#    iterates through the data and stops in that position
#       could do a for loop, with fetchone() inside to get everything neatly


# EXPERIMENTING

test_top = engine.execute('SELECT TOP(5) * FROM Products;')

test_top_results = test_top.fetchall()
print(test_top_results)

# can use either .fetchmany() outside or top() inside


# # adding in sorting???
# test_sorted_top = engine.execute('SELECT TOP(5) * FROM Products ORDER BY Price;')
#
# test_sorted_results = test_sorted_top.fetchall()
# print(test_sorted_results)


# matts stuff

headers = results.keys()
print(headers)
# this is very much like in a dictionary!!!

chai = engine.execute("SELECT * FROM Products Where ProductName = 'Chai'")
print(chai.fetchall())

# can do a join too, same as in sql queries inside the () after engine.execute


# using it all with pandas

query = 'SELECT * FROM Products'
products_df = pd.read_sql_query(query, engine)
print(products_df)

# can create a query and pandas will pass it into the engine
# converts it into a data frame!

# can do everything we were doing with pandas on jupyter notebook

print(products_df.describe())
