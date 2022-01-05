from flask import Blueprint, render_template, redirect, url_for, request, session, flash
import mysql.connector
from interact_with_DB import interact_db


assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates'
                         )


# insert query
@assignment10.route('/insert', methods=['GET', 'POST'])
def insert_func():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        query1 = "SELECT * FROM users WHERE email='%s'" % (email)
        db1 = interact_db(query1, 'fetch')
        if db1 == []:
            query2 = "INSERT INTO users(name,email) VALUES ('%s','%s')" % (name, email)
            interact_db(query2, query_type='commit')
            flash("משתמש הוכנס בהצלחה!")
            return redirect('assignment10')
        else:
            flash("כתובת מייל כבר קיימת")
            return redirect('assignment10')


# delete query
@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        email = request.args['email']
        query1 = "SELECT * FROM users WHERE email='%s'" % (email)
        db1 = interact_db(query1, 'fetch')
        if db1!=[]:
            query2 = "DELETE FROM users WHERE email='%s'" % (email)
            interact_db(query2, query_type='commit')
            flash("משתמש נמחק בהצלחה!")
            return redirect('assignment10')
        else:
            flash("כתובת מייל לא קיימת")
            return redirect('assignment10')


# update query
@assignment10.route('/update', methods=['GET', 'POST'])
def update_user():
    email = request.form['email']
    name = request.form['name']
    query = "SELECT * FROM users WHERE email='%s'" % (email)
    db1= interact_db(query, 'fetch')

    if request.method == 'POST' and db1!=[]:
        query = "UPDATE users SET name = '%s' WHERE email='%s'" % (name, email)
        interact_db(query, query_type='commit')
        flash("העדכון בוצע בהצלחה")
        return redirect('assignment10')
    else:
        flash("כתובת מייל לא קיימת ")
        return redirect('assignment10')


# list query
@assignment10.route('/assignment10')
def user_list():
    session['massage'] = ''
    query = "SELECT * FROM users"
    session['query_results'] = interact_db(query, 'fetch')
    return render_template('assignment10.html')