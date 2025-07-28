import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='mydatabase'  
)
mycursor = mydb.cursor()
name=input("enter name:")
id=input("enter id:")
mycursor.execute("UPDATE users SET name=%s WHERE id=%s",(name,id),)
mydb.commit()
final=mycursor.execute("SELECT * FROM users")
results=mycursor.fetchall()
print(results)


