from flask import Flask, redirect, url_for
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to my website!'

@app.route('/home')
def hello_home():
    return redirect('/')

@app.route('/myweb')
def my_web():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


