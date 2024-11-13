from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def hello(name=None):
    return render_template('remindr-web-flask-app.html', person=name)

@app.route("/")
def hello_world():
    return hello("Greg")

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.debug('Login in process...')

    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def show_the_login_form():
    return render_template('login.html')

def do_the_login():
    username = request.form['username']
    if 'username' in session:
        return render_template('login.html', username_in_session=session["username"])
    else:
        session['username'] = username
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)