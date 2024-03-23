#!/usr/bin/python3
'''
    starts a Flask web application
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' displays HBNB '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_int_html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    odven = 'odd'
    if n % 2 == 0:
        odven = 'even'
    return render_template('6-number_odd_or_even.html', n=n, odven=odven)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
