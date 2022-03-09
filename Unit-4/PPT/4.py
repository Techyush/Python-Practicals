import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host="localhost",database="py",user="root",password="")
    mysql_insert_query="""INSERT INTO laptop (Id, Name, Price, Purchase_date) VALUES (10, "Lenovo", 30880, "2020-04-15")"""
    cursor = connection.cursor()
    cursor.execute(mysql_insert_query)
    connection.commit()
    print(cursor.rowcount,"Record inserted in table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert data {}".format(error))

finally:
    if(connection.is_connected()):
        connection.close()
        print("Connection is closed")