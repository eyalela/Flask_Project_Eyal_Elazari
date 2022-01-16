from flask import Blueprint, Flask, render_template, url_for, redirect
from flask import request, session
from flask import jsonify
import mysql.connector
import json
import requests
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '421992'

from assignment10 import assignment10
app.register_blueprint(assignment10)

query1 ="DELETE FROM users"
query2 = "INSERT INTO users(name, email) VALUES ( 'David', 'david@gmail.com'),( 'Haim', 'haim@gmail.com'),( 'Baruch', 'baruch@gmail.com'),( 'Moshe', 'moshe@gmail.com'),( 'Israel', 'israel@gmail.com') "
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

@app.route('/assignment11/users')
def assignment11_users_func():
    query = "SELECT * FROM users"
    query_result = interact_db(query, 'fetch')
    results = json.dumps(query_result)
    return render_template('/assignment11.html', user_list=results, )


def get_users_backend(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@app.route('/assignment11/outer_source', methods=['POST', 'GET'])
def outer_source_func():
    if "frontend" in request.form:
        number = int(request.form["frontend"])
        return render_template('assignment11_outer_source.html', frontend=number)
    elif "backend" in request.form:
        number = int(request.form["backend"])
        user = get_users_backend(number)
        return render_template('assignment11_outer_source.html', backend=user)
    else:
        return render_template('assignment11_outer_source.html', default="default")

@app.route('/assignment12/restapi_users', defaults={'USER_ID':-1})


@app.route('/assignment12/restapi_users/<int:USER_ID>')
def restapi_func(USER_ID):
    if USER_ID == -1:
        users_dict={}
        query = "SELECT * FROM users ; "
        query_result = interact_db(query, 'fetch')
        for user in query_result:
            users_dict[f'user_{user.id}'] = {
                'status': 'success',
                'name': user.name,
                'email': user.email
            }
    else:
        query = "SELECT * FROM users where id=%s;" %USER_ID
        query_result = interact_db(query, 'fetch')
        if len(query_result)==0:
            users_dict = {
                'status': 'failed',
                'massege': 'user not found'
            }
        else:
            users_dict = {
                'status': 'success',
                'name': query_result[0].name,
                'email': query_result[0].email
            }
    return jsonify(users_dict)



if __name__ == "__main__":
    app.run(debug=True)

