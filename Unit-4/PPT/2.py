import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", database="py", user="root", password="")

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're Connected to ", record)

except Error as e:
    print("Error: ", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL Connection is closed")
