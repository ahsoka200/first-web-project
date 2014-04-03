import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<strong>Hello World!</strong>'

@app.route('/chris')
def chris():
	return "hi"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User ' + username


def page(html):
	return render_template('header.html') + html + render_template('footer.html')