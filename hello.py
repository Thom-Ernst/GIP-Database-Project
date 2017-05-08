import mysql.connector
from flask import Flask
app = Flask(__name__)

conex = mysql.connector.connect(user='imma', password='imma', host='127.0.0.1', database='GIP-Schema')

# cur = conex.cursor()
# cur.execute("SELECT comment.id, name, content FROM `GIP-Schema`.user  INNER join `GIP-Schema`.comment ON user.id = user_id  ORDER BY comment.id ASC;")
# row = cur.fetchone()
# for item in row:
#     output = row
#     row = cur.fetchone()

@app.route('/')
def hello_world():
    global conex
    cur = conex.cursor()
    cur.execute(
        "SELECT comment.id, name, content FROM `GIP-Schema`.user  INNER join `GIP-Schema`.comment ON user.id = user_id  ORDER BY comment.id ASC;")
    row = cur.fetchone()
    string = str(row[1])
    return string
