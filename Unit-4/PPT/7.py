import mysql.connector
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='py', user='root', password='')
    cursor = connection.cursor()
    print("Before updating a record ")
    sql_select_query = """select * from laptop where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update Query

    sql_update_query = """Update laptop set Price = 7000 where id = 1"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")
    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))

finally:
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
