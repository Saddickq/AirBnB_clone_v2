#!/usr/bin/python3
"""Routes
"""
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
