# Install MySQL
# pip install mysql
# pip install mysql-conntector
# pip install mysql-conntector-python

import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd = "password1234"
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create the database
cursorObject.execute("CREATE DATABASE elderco")
print("Database created successfully!")