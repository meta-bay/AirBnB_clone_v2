#!/usr/bin/python3
'''
    hbnb filters
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    s = storage.all(State)
    am = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', s=s, am=am)


@app.teardown_appcontext
def app_teardown(arg=None):
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
