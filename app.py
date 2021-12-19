from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def cv():
    return render_template('CV.html')

@app.route('/assignment8')
def assignment8():
    #DB
    return render_template('assignment8.html', hobby='football', music='Hip Hop', languages=['Hebrew', 'English'])

if __name__ == "__main__":
    app.run(debug=True)
