import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='mydatabase'  
)
mycursor = mydb.cursor()

gmail_input=input("enter the mail to insert:")
mycursor.execute("SELECT * FROM users",(gmail_input),)
results = mycursor.fetchall()
print(results)
if gmail_input in results:
    print("already exists")
else:
   print( query=mycursor.execute("INSERT INTO users (gmail) VALUES (?)",(gmail_input),))



