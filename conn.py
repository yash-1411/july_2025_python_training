import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='mydatabase'  
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
