#!/usr/bin/python3
'''
    starts a Flask web application
'''
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello():
    ''' displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' displays HBNB '''
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    return 'c {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
