from flask import Blueprint, Flask, render_template, url_for, redirect
from flask import request, session
import mysql.connector
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '421992'

from assignment10 import assignment10
app.register_blueprint(assignment10)
query1 ="DELETE FROM users"
query2 = "INSERT INTO users(name, email) VALUES ( 'Yizhar', 'Yizhar@gmail.com'),( 'Lili', 'Lili@gmail.com') "
interact_db(query1, query_type='commit')
interact_db(query2, query_type='commit')

@app.route('/')
def cv():
    return render_template('CV.html')

@app.route('/assignment8')
def assignment8():
    #DB
    return render_template('assignment8.html', hobby='football', music='Hip Hop', languages=['Hebrew', 'English'])

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    email = ''
    userFound = False
    users = (
            {'name': 'David', 'email': 'david@gmail.com'},
            {'name': 'Baruch', 'email': 'baruch@gmail.com'},
            {'name': 'Haim', 'email': 'haim@gmail.com'},
            {'name': 'Moshe', 'email': 'moshe@gmail.com'},
            {'name': 'Israel', 'email': 'israel@gmail.com'})


    if request.method == 'GET':
        if 'name' in request.args:
                username = request.args['name']
                userFound = True

    if request.method == 'POST':
          username = request.form['username']
          session['logged_in'] = True
          session['username'] = username
    return render_template('assignment9.html', request_method=request.method, username=username, email=email, users=users, userFound=userFound)


@app.route('/logout')
def logout():
    session['username'] = ''
    session['logged_in'] = False
    return render_template('assignment9.html')

if __name__ == "__main__":
    app.run(debug=True)

