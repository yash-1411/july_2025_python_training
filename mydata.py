import sqlite3
conn=sqlite3.connect("mydata.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",("Alice",25))
cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",("Bob",30))
conn.commit()
conn.close()