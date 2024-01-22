#!/usr/bin/env python3
# app.py
# here we will have route definitions and logic for our API

# Standard library imports
import os

# Remote library imports
# Local imports
from config import api, app, db
from dotenv import load_dotenv
from flask import jsonify, make_response, request
from flask_restful import Resource
from marshmallow import Schema, fields, validate
from models import Category, Order, OrderDetail, Product, User
from sqlalchemy.exc import IntegrityError

# Builds app, set attributes
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'app.db')}"
)
load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return "<h1>Mont Luxe Watch Company Ecommerce Platform</h1>"


# TESTED ✅
class Products(Resource):
    # TESTED ✅
    def get(self):
        try:
            products = [product.to_dict() for product in Product.query.all()]
            return make_response({"products": products}, 200)
        except Exception as error:
            return make_response({"error": str(error)}, 500)

    # TESTED ✅
    def post(self):
        product_data = request.get_json()
        try:
            required_fields = [
                "name",
                "description",
                "price",
                "item_quantity",
                "image_url",
                "imageAlt",
            ]
            if not all(field in product_data for field in required_fields):
                return make_response({"error": "Missing required fields"}, 400)

            new_product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                item_quantity=product_data["item_quantity"],
                image_url=product_data["image_url"],
                imageAlt=product_data["imageAlt"],
            )
            db.session.add(new_product)
            commit_session(db.session)
            return make_response({"new_product": new_product.to_dict()}, 201)
        except IntegrityError:
            return make_response(
                {"error": "Product creation failed due to a database error."}, 400
            )
        except Exception as error:
            return make_response({"error": str(error)}, 500)


class ProductByID(Resource):
    # TESTED ✅
    def get(self, id):
        product = Product.query.get(id)
        if product:
            return make_response(product.to_dict(), 200)
        else:
            return make_response({"error": "Product not found"}, 404)

    # TESTED ✅
    def patch(self, id):
        product = Product.query.get(id)

        if product:
            data = request.get_json()

            try:
                for attr in data:
                    setattr(product, attr, data[attr])

                commit_session(db.session)

                return make_response(product.to_dict(), 202)

            except ValueError:
                return make_response({"errors": ["validation errors"]}, 400)
        else:
            return make_response({"error": "Product not found"}, 404)

    # TESTED ✅
    def delete(self, id):
        try:
            product = Product.query.get(id)
            if product:
                db.session.delete(product)
                commit_session(db.session)
                return jsonify({}), 204
            else:
                return make_response({"error": "Product not found"}), 404
        except Exception as error:
            return make_response({"error": str(error)}), 500


class Users(Resource):
    # TESTED ✅
    def get(self):
        return make_response([user.to_dict() for user in User.query.all()], 200)

    # TESTED ✅
    def post(self):
        user_data = request.get_json()
        try:
            new_user = User(
                username=user_data["username"],
                email=user_data["email"],
                shipping_address=user_data.get("shipping_address", ""),
                shipping_city=user_data.get("shipping_city", ""),
                shipping_state=user_data.get("shipping_state", ""),
                shipping_zip=user_data.get("shipping_zip", ""),
            )
            new_user.password = user_data["password"]
            db.session.add(new_user)
            commit_session(db.session)  # Use your custom commit_session function

            return make_response({"message": "User created successfully"}, 201)
        except IntegrityError:
            return make_response(
                {"error": "User creation failed due to a database error."},
                400,
            )
        except Exception as error:
            return make_response({"error": "User creation failed: " + str(error)}, 500)


# User Schema
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(
        load_only=True, required=True, validate=validate.Length(min=6)
    )
    shipping_address = fields.Str()
    shipping_city = fields.Str()
    shipping_state = fields.Str()
    shipping_zip = fields.Str()
    orders = fields.Nested("OrderSchema", many=True, exclude=("user",))

    def __repr__(self):
        return f"<User {self.username}>"


class Orders(Resource):
    def get(self):
        try:
            orders = Order.query.all()
            return make_response([order.to_dict() for order in orders], 200)
        except Exception as error:
            return make_response({"error": str(error)}, 500)


# Order Schema
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(load_only=True)
    created_at = fields.DateTime(dump_only=True)
    order_details = fields.Nested("OrderDetailSchema", many=True, exclude=("order",))

    def __repr__(self):
        return f"<Order {self.id}>"


class OrderDetails(Resource):
    def get(self):
        try:
            order_details = OrderDetail.query.all()
            return make_response([detail.to_dict() for detail in order_details], 200)
        except Exception as error:
            return make_response({"error": str(error)}, 500)


# OrderDetail Schema
class OrderDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(load_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))

    def __repr__(self):
        return f"<OrderDetail Order: {self.order_id}, Product: {self.product_id}>"


# This utility function attempts to commit changes to the database but if an error occurs it will roll back the session to avoid leaving the database in an inconsistent state. Then it re-raises the exception to be handled by the caller.
def commit_session(session):
    try:
        session.commit()
    except IntegrityError as exc:
        session.rollback()
        raise exc


# This function is used to create a category if it does not exist. It first tries to find the category by name. If it's not found, it creates a new one, commits the session
def get_or_create_category(category_name):
    category = (
        db.session.query(Category).filter_by(name=category_name).first()
    )  # first row is more effcient than all() as it only takes one in memory.Filters one where the anem matches.
    if category is None:
        category = Category(name=category_name)
        db.session.add(category)
        commit_session(db.session)
    return category


class Login(Resource):
    def post(self):
        data = request.get_json()

        if not all(key in data for key in ("username", "password")):
            return make_response({"error": "Username and password are required"}, 400)

        username = data["username"]
        password = data["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            return make_response({"message": "Login successful"}, 200)
        else:
            return make_response({"error": "Invalid credentials"}, 401)


api.add_resource(Products, "/products")
api.add_resource(Users, "/users")
api.add_resource(Orders, "/orders")
api.add_resource(OrderDetails, "/order_details")
api.add_resource(ProductByID, "/products/<int:id>")
api.add_resource(Login, "/login")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
