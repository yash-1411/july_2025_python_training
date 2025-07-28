import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='roottoor',
    database='mydatabase'
)

mycursor = mydb.cursor()

email_input = input("Enter the email: ")

query = "SELECT * FROM users WHERE gmail = %s"
mycursor.execute(query, (email_input,))

results = mycursor.fetchall()

if results:
    print("Email exists in the database.")
else:
    print("Email does not exist.")

mycursor.close()
mydb.close()
