import mysql.connector
from flask import Flask, render_template
app = Flask(__name__)

conex = mysql.connector.connect(user='imma', password='imma', host='127.0.0.1', database='GIP-Schema')

# cur = conex.cursor()
# cur.execute("SELECT comment.id, name, content FROM `GIP-Schema`.user  INNER join `GIP-Schema`.comment ON user.id = user_id  ORDER BY comment.id ASC;")
# row = cur.fetchone()
# for item in row:
#     output = row
#     row = cur.fetchone()


@app.route('/')
def main():
    return render_template('index.html')
# def hello_world():
#     global conex
#     cur = conex.cursor()
#     cur.execute(
#         "SELECT comment.id, name, content FROM `GIP-Schema`.user  INNER join `GIP-Schema`.comment ON user.id = user_id  ORDER BY comment.id ASC;")
#     row = cur.fetchone()
#     string = str(row)
#     return string
