import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", database="py", user="root", password="")
    mysql_Create_Table_Query = """CREATE TABLE Laptop(Id int(11)NOT NULL, Name varchar(250)NOT NULL, Price float NOT NULL, Purchase_date Date NOT NULL, PRIMARY KEY(id))"""
    cursor = connection.cursor()
    result = cursor.execute(mysql_Create_Table_Query)
    print("Table Created")
except mysql.connector.Error as error:
    print("Failed to create table: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")
