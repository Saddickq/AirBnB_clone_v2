#!/usr/bin/python3
"""Routes
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """route to home"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def something(text):
    """display “C ” followed by the value of the text variable"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/")
def python(text="is cool"):
    """display Python , followed by the value of the text variable """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n is a number only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template('even.html', num=n)
    return render_template('odd.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
