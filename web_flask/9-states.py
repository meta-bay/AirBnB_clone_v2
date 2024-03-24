#!/usr/bin/python3
'''
    states and state
'''
from models.state import State
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
