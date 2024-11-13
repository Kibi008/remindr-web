from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def hello(name=None):
    return render_template('remindr-web-flask-app.html', person=name)

@app.route("/")
def hello_world():
    return hello("Greg")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def show_the_login_form():
    return render_template('login.html')

def do_the_login():
    return "Logged"

if __name__ == '__main__':
    app.run(debug=True)