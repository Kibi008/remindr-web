from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)



def hello(name=None):
    return render_template('remindr-web-flask.html', person=name)

@app.route("/")
def hello_world():
    return "<h1>
</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)