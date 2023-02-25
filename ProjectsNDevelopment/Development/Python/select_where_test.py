import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythontest"
)

mycursor = mydb.cursor()

print("1 record inserted, ID:", mycursor.lastrowid)
sql='select name,age from customers where age is not null'
mycursor.execute(sql)

myrestul = mycursor.fetchone()

sql2 = "select name,address,age from customers where name like 'P%'"
mycursor.execute(sql2)
myresult2 = mycursor.fetchall()


for x in myrestul:
    print (x)

for y in myresult2:
    print(y)

