import mysql.connector
def insert_data(id,name,email):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='roottoor',
        database='mydatabase'  
    )
    mycursor=mydb.cursor()
    sql="INSERT INTO user1(id,name,email)"
    "VALUES(%S,%S,%S)"
    val=(id,name,email)
    cursor.execute(sql,val)