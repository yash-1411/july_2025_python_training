from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route('/getData')#fn to give in json format
def getData():
    id = request.args.get("id")
    cur = mysql.connection.cursor()

    if id is None:
        sql = "SELECT * FROM users"
        cur.execute(sql)
    else:
        sql = "SELECT * FROM users WHERE id = %s"
        cur.execute(sql, (id,))

    results = cur.fetchall()
    cur.close()
    return jsonify(results)


@app.route('/getDataInHtml')#fn to give in html table format
def getDataInHtml():
    id = request.args.get("id")
    cur = mysql.connection.cursor()

    if id is None:
        sql = "SELECT * FROM users"
        cur.execute(sql)
    else:
        sql = "SELECT * FROM users WHERE id = %s"
        cur.execute(sql, (id,))

    results = cur.fetchall()
    cur.close()
    return render_template("userlist.html",userlist=results)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/myname')
def printing():
    return "hello world"


@app.route('/myhtml')
def myhtml():
    return render_template("home.html") 


@app.route('/mydetails', methods=["GET", "POST"])
def mydetails():
    name = request.args.get("name")
    city = request.args.get("city")
    address = request.args.get("address")
    return f"{name} {city} {address}"

@app.route('/register_save', methods=["GET", "POST"])
def register_save():
    if request.method == "GET":
        return render_template("register.html")
    else:
        gmail = request.form.get("gmail")
        passwords = request.form.get("passwords")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO users(gmail, passwords) VALUES (%s, %s)"
        val = (gmail, passwords)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return "Register success!"


@app.route('/userDetails')
def userDetails():
    id = request.args.get("id")
    
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM users WHERE id = %s"
    cur.execute(sql, (id,))
    
    results = cur.fetchone() 
    print(results)
    cur.close()
    
    return render_template(
        "user_detail.html",
        id=results[0],
        name=results[1],
        gmail=results[2],
        passwords=results[3]
    )
if __name__ == "__main__":
    app.run(debug=True)




