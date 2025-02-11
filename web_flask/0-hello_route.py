#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function to display a message on a given route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
