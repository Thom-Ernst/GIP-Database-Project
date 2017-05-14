import re
from flask import Flask, render_template, json, request
from __main__ import gamelogic
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'imma'
app.config['MYSQL_DATABASE_PASSWORD'] = 'imma'
app.config['MYSQL_DATABASE_DB'] = 'GIP-Schema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# pre-runtime classes and variables here:


gm = gamelogic()

class db:
    con = mysql.connect()
    cur = con.cursor()

    def fo(self, query):
        self.cur.execute(query)
        return re.search('^\((\d*),\)$', str(self.cur.fetchone())).group(1)

    def fa(self, query):
        self.cur.execute(query)
        return str(self.cur.fetchall())

    def close(self):
        self.cur.close()
        self.con.close()


# app.route functions
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        gm.p_name = request.form['inputName']
        gm.p_lastname = request.form['inputLastname']

        db().cur.callproc('sp_createUser', (gm.p_name, gm.p_lastname))
        data = db().cur.fetchall()

        if len(data) is 0:
            db().con.commit()
            gm.p_user_id = db().fo('SELECT id FROM `GIP-Schema`.user WHERE name = \'{0}\''.format(gm.p_name))
            gm.p_ronde = 0
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/quizApp')
def quizApp():
    gm.p_ronde += 1
    gm.assignvars()
    if gm.p_lastresult == 2:
        gamestr = 'Incorrect! The correct answer was: {0}.'.format(gm.dj.trackChosen.name)
    elif gm.p_lastresult == 1:
        gamestr = 'That answer is Correct! +1 to your score!'
    else:
        gamestr = 'Welcome to PyQuiz, {0}! Choose the song you think is playing, you play 10 rounds.'.format(gm.p_user)

    return render_template('quiz.html',
                           gamestring = gamestr,
                           file = gm.p_file,
                           song1 = gm.songs(0),
                           song2 = gm.songs(1),
                           song3 = gm.songs(2),
                           song4 = gm.songs(3),
                           round = gm.p_ronde,
                           lastresult = gm.p_lastresult)


@app.route('/checkAnswer', methods=['POST'])
def checkAnswer():
    try:
        answer = request.form['answer'] if 'answer' in request.form else None
        if answer == str(gm.dj.trackKey):
            gm.p_lastresult = 1
            return 'Answer Correct! +1 to your score!'

        else:
            gm.p_lastresult = 2
            return 'Answer incorect!'

    except Exception as e:
        return 'something went wrong! (checkAnswer)'

    finally:
        if gm.p_ronde == 10:
            sendScore()

        else:
            quizApp()


@app.route('/sendScore')
def sendScore():
    try:
        db().cur.callproc('sp_createScoreEntry', (gm.p_score, gm.p_user_id))
        data = db().cur.fetchall()

        if len(data) is 0:
            db().con.commit()
            return json.dumps({'message': 'Score submitted.'})
        else:
            return json.dumps({'error': str(data[0])})

    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/scoreBoard')
def showScoreboard():
    query = db().fa('SELECT name, score '
                  'FROM `GIP-Schema`.scoreboard '
                  'INNER JOIN `GIP-Schema`.user ON user_id = user.id '
                  'ORDER BY score DESC')
    name1 = db().fo('')
    name2 = db().fo('')
    name3 = db().fo('')
    score1 = db().fo('')
    score2 = db().fo('')
    score3 = db().fo('')
    return render_template('scoreboard.html',
                           name1 = name1,
                           name2 = name2,
                           name3 = name3,
                           score1 = score1,
                           score2 = score2,
                           score3 = score3)
