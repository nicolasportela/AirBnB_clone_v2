#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def html5():
    """function 9 to display an html page"""""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()

if __name__ == '__main__':
    app.run()
