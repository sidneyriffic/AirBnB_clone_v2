#!/usr/bin/python3
"""The / route"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """root folder route"""
    return "Hello, HBNB!"


app.run()
