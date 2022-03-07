import mysql.connector

mydb = mysql.connector.connect(host="localhost", database="py", user="root", passwd="")

print(mydb)
