from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session
from flask_moment import Moment
from datetime import datetime

""" Paramétrages app """

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Init moment
moment = Moment(app)
# Init Bootstrap
#Bootstrap(app)

""" Routing """

@app.route("/")
def hello_world():    
    return render_template('remindr-web-flask-app.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.debug('Login in process...')

    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    app.logger.debug('Logout in process...')
    session.pop("username", None)
    return redirect("/") 
    
    
""" Autres méthodes """

def show_the_login_form():
    return render_template('login.html')

def do_the_login():
    username = request.form['username']
    app.logger.debug(username)
    if 'username' in session:
        username_in_session=session["username"]
        app.logger.debug(username_in_session)
        if username != username_in_session:
            session['username'] = username
            username_in_session = username # On prend le plus récent, celui qui vient d'être envoyé par le formulaire        
    else:
        session['username'] = username
        username_in_session = session['username']
        app.logger.debug(username_in_session)
    return render_template('login.html', username_in_session=username_in_session)

if __name__ == '__main__':    
    app.run(debug=True)