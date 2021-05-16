import pyodbc

#creating the connection string
connection_string = (
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=mydb;'
    'UID=myusername;'
    'PWD=mypassword;'
)

#creating connection object
conn = pyodbc.connect(connection_string)

#creating cursor object
cursor = conn.cursor()

#using cursor to retrieve some data from a table
query = "SELECT * FROM some_table"
cursor.execute(query)
#saving the query results to a variable
results = cursor.fetchall()
#doing something with the results
for result in results:
    print(result)

#using cursor to INSERT new data into a table
query = "INSERT INTO some_table (some_column, another_column) VALUES ('data for some_column', 'data for another_column')"
cursor.execute(query)

#using cursor to UPDATE existing data 
query = "UPDATE some_table SET some_column = 'some value' WHERE id = some_id"
cursor.execute(query)

#committing all changes and closing the connection
conn.commit()
conn.close()