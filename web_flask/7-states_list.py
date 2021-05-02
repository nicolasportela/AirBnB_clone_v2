#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def html4():
    """function 8 to display an html page"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()

if __name__ == '__main__':
    app.run()
