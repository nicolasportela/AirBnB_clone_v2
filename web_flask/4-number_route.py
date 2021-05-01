#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function to display a message on a given route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function 2 to display a message on a given route"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """function 3 to display a message on a given route"""
    text = text.replace("_", " ")
    return 'C %s' % text

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """function 4 to display a message on a given route"""
    text = text.replace("_", " ")
    return 'Python %s' % text

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function 5 to display a message on a given route"""
    return '%d is a number' % n

app.run()
