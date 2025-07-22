import sqlite3
conn=sqlite3.connect("mydata.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users where id=1")
conn.commit()
conn.close()