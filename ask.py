import sqlite3
conn=sqlite3.connect("mydata.db")
cursor = conn.cursor()
count=input("enter number of users :")
for i in count:
    name=input("enter name")
    age=input("enter age")
    cursor.execute("INSERT INTO users (name,age) VALUES(?,?)",(name,age))
conn.commit()
conn.close()