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
    strict_slashes = False
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' displays HBNB '''
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    strict_slashes = False
    c = 'c '
    for i in text:
        if i == '_':
            c = c + ' '
        else:
            c = c + i
    return c


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
