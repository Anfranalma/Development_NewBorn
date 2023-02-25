import mysql.connector

'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
'''

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythontest'
)

mycursor = mydb.cursor()

#mycursor.execute("Create Database PythonTest")
mycursor.execute("Show databases")


for x in mycursor:
    print(x)

#mycursor.execute('create table customers(name varchar(255), address varchar(255))')

mycursor.execute('drop table customers')
mycursor.execute('create table customers(id int auto_increment primary key, name varchar(255), address varchar(255))')
mycursor.execute('alter table customers add column age int')
