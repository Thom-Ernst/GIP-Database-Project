from flask import Flask, render_template, json, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'imma'
app.config['MYSQL_DATABASE_PASSWORD'] = 'imma'
app.config['MYSQL_DATABASE_DB'] = 'GIP-Schema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        p_name = request.form['inputName']
        p_lastname = request.form['inputLastname']

        con = mysql.connect()
        cur = con.cursor()
        cur.callproc('sp_createUser', (p_name, p_lastname))
        data = cur.fetchall()

        if len(data) is 0:
            con.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

    except Exception as e:
        return json.dumps({'error': str(e)})

    finally:
        if con and cur:
            cur.close()
            con.close()


@app.route('/quizApp')
def quizApp():
    return render_template('quiz.html')


@app.route('/checkAnswer', methods=['GET'])
def checkAnswer():
    try:
        answer = request.data

        if answer == 1:
            return 'ham'

    except Exception as e:
        return 'foo bar'