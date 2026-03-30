# Date: 29/03/2026

'''
Basic steps to use XAMPP & phpMyAdmin:

1. Install XAMPP (provides Apache server + MySQL database).
2. Open XAMPP Control Panel.
3. Start Apache and MySQL services.
4. Open a browser.
5. Type http://localhost/
6. Click on phpMyAdmin (database GUI).
7. Create a database first.
8. Create tables and define columns (headers).
9. Use VARCHAR instead of string in MySQL.
10. Always define length for data types (e.g., VARCHAR(50)).
11. Learn INSERT, UPDATE, DELETE queries.
12. WHERE clause is used to filter rows.
13. Be careful: without WHERE, entire table may be affected.
14. No Ctrl+Z → changes are permanent unless backed up.
15. For Python connection: install mysql connector:
    pip install mysql-connector-python
16. This allows Python to connect with MySQL database.
'''

# Day 18 - Using Database from Python

# Import MySQL connector library
import mysql.connector

# Create connection to MySQL database
db = mysql.connector.connect(
    user="root",          # MySQL username
    host="localhost",     # Server location (local machine)
    # password not set here
    port=3306,            # Default MySQL port
    database="feb22python" # Database name
)

# Create a cursor object (used to execute SQL queries)
terminal = db.cursor()


# ---------------- INSERT OPERATION ----------------
'''
# SQL query to insert data into table
insert = "INSERT INTO student (name, address, phone) VALUES ('Seema', 'Gorkhar', '1234')"

terminal.execute(insert)   # Execute query
db.commit()                # Save changes permanently
'''


# ---------------- UPDATE OPERATION ----------------
'''
# Update specific row using WHERE
update = "UPDATE student SET address='nepal' WHERE id=1"

terminal.execute(update)   # Execute query
db.commit()                # Save changes
print(db)                  # Print connection object
'''


# ---------------- DELETE OPERATION ----------------
'''
# Delete a row using condition
delete = "DELETE FROM student WHERE id=0"

terminal.execute(delete)   # Execute query
db.commit()                # Save changes
print(db)
'''


# ---------------- FETCH (READ DATA) ----------------

# Select all columns from table
fetch = "SELECT * FROM student"

# Alternative: select specific columns only
# fetch = "SELECT name, address FROM student"

terminal.execute(fetch)     # Execute SELECT query

result = terminal.fetchall()  # Fetch all rows (list of tuples)

# Print each row in formatted way
for i in result:
    # i[0] = id, i[1] = name, i[2] = address
    output = f'id = {i[0]} name = {i[1]} address = {i[2]}'
    print(output)


# ---------------- ERROR HANDLING ----------------

try:
    print(1 + "2")  # This will cause TypeError (int + string)

except NameError:
    print("Name error occurred")

except ZeroDivisionError:
    print("Division by zero error")

except TypeError as message:
    print(message)  # Print actual error message

except:
    print("Something went wrong")


'''
Description:

- This program demonstrates how to connect Python with MySQL.
- It shows CRUD operations:
  C → Create (INSERT)
  R → Read (SELECT)
  U → Update (UPDATE)
  D → Delete (DELETE)
- Uses cursor to execute SQL queries.
- Uses commit() to permanently save changes.
- Uses fetchall() to retrieve data from database.
- Includes basic exception handling to manage runtime errors.

Tip:
Always use WHERE clause in UPDATE and DELETE to avoid affecting entire table.
'''