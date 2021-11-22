import mysql.connector


# ######################### creating databse ###################################
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms"
)

cursor = db.cursor()

## creating a databse called 'pysql'
cursor.execute("CREATE DATABASE pysql")


########################## connect with MySQL ################################
try:
    db = mysql.connector.connect(user='root', password='root', host='localhost', database="pysql")
    print('Connet Successfully')
    cursor = db.cursor()
except mysql.connector.Error as err:
    print("Somthig is wrong")

########################## creating table in database######################### 
cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), user_name VARCHAR(255))")
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()
for table in tables:
    print('You are using table ', table)


####################### Insert data into users table ########################
# defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable

values =  (("JavaScript", "js"), ("Python", "Py"))

## executing the query with values
for value in values:
    cursor.execute(query, value)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")

# ####################### select data from users table ########################

query = "SELECT * FROM users"
## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()
print()
print('Select data is : ')
## Showing the data
for record in records:
    print(record)

# ####################### select data from users table using Where ########################

# defining the Query
query = "SELECT * FROM users WHERE user_name = 'py'"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

print()
print("Using whare condition: ")
## Showing the data
for record in records:
    print(record)

# ####################### delete data from users table ########################

# defining the Query
query = "DELETE FROM users WHERE user_name = 'py'"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

query = "SELECT * FROM users"

cursor.execute(query)

records = cursor.fetchall()

print()
print("After delete some data : ")
for record in records:
    print(record)

# ####################### update data into users table ########################

## defining the Query
query = "UPDATE users SET name = '123' WHERE user_name = 'js'"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

query = "SELECT * FROM users"

cursor.execute(query)

records = cursor.fetchall()

print()
print("After update  data : ")
for record in records:
    print(record)



