#!/usr/bin/env python3
# app.py

# Standard library imports
import os

# Local imports
from config import app, db

# Remote library imports
from config import app, db, api
from models import Order, OrderDetail, Product, User
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from utils import commit_session
from flask import jsonify, make_response, request

# Builds app, set attributes
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'app.db')}"
)

# Add your model imports


# Views go here!


@app.route("/")
def index():
    return "<h1>Mont Luxe Watch Company Ecommerce Platform</h1>"


class Products(Resource):
    def get(self):
        try:
            products = [product.to_dict() for product in Product.query.all()]
            return make_response(jsonify(products), 200)
        except Exception as error:
            return make_response(
                jsonify({"error": "Failed to fetch products: " + str(error)}), 500
            )

    def post(self):
        product_data = request.get_json()
        try:
            new_product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                item_quantity=product_data["item_quantity"],
                image_url=product_data["image_url"],
            )
            db.session.add(new_product)
            commit_session(db.session)
            return make_response(jsonify(new_product.to_dict()), 201)
        except IntegrityError:
            return make_response(
                jsonify({"error": "Product creation failed due to a database error."}),
                400,
            )
        except Exception as error:
            return make_response(
                jsonify({"error": "Product creation failed: " + str(error)}), 500
            )

    def patch(self, id):
        data = request.get_json()
        try:
            updated_records = Product.query.filter_by(id=id).update(data)
            if updated_records:
                commit_session(db.session)
                product = Product.query.get(id)
                return jsonify(product.to_dict()), 200
            else:
                return jsonify({"error": "Product not found"}), 404
        except IntegrityError:
            return jsonify({"error": "Database Integrity Error"}), 400
        except Exception as error:
            return jsonify({"error": str(error)}), 500

    def delete(self, id):
        try:
            product = Product.query.get(id)
            if product:
                db.session.delete(product)
                commit_session(db.session)
                return jsonify({}), 204
            else:
                return jsonify({"error": "Product not found"}), 404
        except Exception as error:
            return jsonify({"error": str(error)}), 500


class Users(Resource):
    def get(self):
        try:
            users = User.query.all()
            serialized_users = [user.to_dict() for user in users]
            return jsonify(serialized_users), 200
        except Exception as error:
            return jsonify({"error": "Failed to fetch users"}), 500

    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                username=data["username"],
                email=data["email"],
                SimplePassword=data["SimplePassword"],  # Consider hashing this password
                shipping_address=data["shipping_address"],
                shipping_city=data["shipping_city"],
                shipping_state=data["shipping_state"],
                shipping_zip=data["shipping_zip"],
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except IntegrityError:
            return make_response(
                jsonify({"error": "A user with these details already exists"}), 400
            )
        except Exception as error:
            return make_response(jsonify({"error": str(error)}), 500)


class Orders(Resource):
    def get(self):
        try:
            orders = [order.to_dict() for order in Order.query.all()]
            return jsonify(orders), 200
        except Exception as error:
            return jsonify({"error": str(error)}), 500


class OrderDetails(Resource):
    def get(self):
        try:
            order_details = [detail.to_dict() for detail in OrderDetail.query.all()]
            return jsonify(order_details), 200
        except Exception as error:
            return jsonify({"error": str(error)}), 500


api.add_resource(Products, "/products")
api.add_resource(Users, "/users")
api.add_resource(Orders, "/orders")
api.add_resource(OrderDetails, "/order_details")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
