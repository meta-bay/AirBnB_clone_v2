#!/usr/bin/python3
'''
    states and state
'''
from models.state import State
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states')
def states_list():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_by_id(id):
    states = storage.all(State).values()
    the_state = None
    for state in states:
        if state.id == id:
            the_state = state
    return render_template('9-states.html', states=the_state)


@app.teardown_appcontext
def app_teardown(arg=None):
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
