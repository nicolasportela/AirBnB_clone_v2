#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def html6(state_id=None):
    """function 10 to display an html page"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()

if __name__ == '__main__':
    app.run()
