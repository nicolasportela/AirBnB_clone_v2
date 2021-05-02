#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):
    """function 6 to display a message on a given route"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html2(n):
    """function 7 to display a message on a given route"""
    if n % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    return render_template('6-number_odd_or_even.html', n=n, oddeven=oddeven)

if __name__ == '__main__':
    app.run()
