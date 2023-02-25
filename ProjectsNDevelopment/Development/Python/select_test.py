import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythontest"
)

mycursor = mydb.cursor()

print("1 record inserted, ID:", mycursor.lastrowid)
mycursor.execute('select name,age from customers')

myrestul = mycursor.fetchone()

for x in myrestul:
    print (x)