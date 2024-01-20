#!/usr/bin/env python3

# Standard library imports

# Local imports
from config import api, app, db

# Remote library imports
from flask import request
from flask_cors import cross_origin
from flask_restful import Resource

# Add your model imports


# Views go here!


@app.route("/")
def index():
    return "<h1>Project Server</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
