import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return page('<strong>Hello World!</strong>')

@app.route('/chris')
def chris():
	return "hi"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User ' + username


def page(html):
	return render_template('header.html') + html + render_template('footer.html')

@app.route('/template')
def template():
	return page('test test test')

@app.route('/about')
def about():
	return page('this is a page about stuff!')

