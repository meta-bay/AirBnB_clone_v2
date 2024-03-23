#!/usr/bin/python3
'''
    hello flask
'''
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    ''' hello function '''
    strict_slashes = False
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
