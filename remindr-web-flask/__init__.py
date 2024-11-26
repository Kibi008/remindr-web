import os
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session
from flask_moment import Moment
from datetime import datetime

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
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

    @app.route("/sb-index")
    def sb_index():    
        return render_template('sb-admin-2/index.html')

    @app.route("/sb-login")
    def sb_login():    
        return render_template('sb-admin-2/login.html')

    @app.route("/sb-admin")
    def sb_admin():    
        return render_template('test-page.html')

    @app.route("/front-dashboard")
    def front_dashboard():    
        return render_template('front-admin/index.html')

        
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

    return app