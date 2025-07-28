import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='mydatabase'  
)
mycursor = mydb.cursor()
take=input("enter the gmail:")
mycursor.execute("SELECT * FROM users WHERE gmail=%s",(take,))
myresult = mycursor.fetchall()
print(myresult)
if myresult:
    print("email exists")
else:
    print("dosent exist")