import mysql.connector

myData=mysql.connector.connect(host="localhost",user="root",passwd="root")

myCursor=myData.cursor()

myCursor.execute("show databases")

for i in myCursor:
 print(i)
