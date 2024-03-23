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
