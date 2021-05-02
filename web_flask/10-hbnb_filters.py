#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def html7():
    """function 11 to display an html page"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()

if __name__ == '__main__':
    app.run()
