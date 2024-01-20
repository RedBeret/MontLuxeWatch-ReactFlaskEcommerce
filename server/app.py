#!/usr/bin/env python3

# Standard library imports
import os

# Local imports
from config import api, app, db

# Remote library imports
from flask import Flask, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from models import Category, Order, OrderDetail, Product, User, db
from sqlalchemy import MetaData

# Builds app, set attributes
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Define metadata, Builds db, seen on other labs
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Builds REST API
api = Api(app)

# Builds CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Add your model imports


# Views go here!


@app.route("/")
def index():
    return "<h1>Mont Luxe Watch Company Ecommerce Platform</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
