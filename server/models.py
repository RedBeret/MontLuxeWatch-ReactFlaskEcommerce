# models.py

# Import necessary modules from SQLAlchemy and SerializerMixin for serialization.
from config import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

# Models go here!
# one to many relationship between order and order details
# one to many relationship between user and orders

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)


# Product Model
# This class represents the products (watches) that we're selling.
# Each product has an ID, name, description, price, quantity, and an image URL. Wonder how they get two images.
class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    item_quantity = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    imageAlt = db.Column(db.String(255))

    product_categories = db.relationship(
        "ProductCategory", back_populates="product", cascade="all, delete-orphan"
    )
    categories = association_proxy("product_categories", "category")

    def __repr__(self):
        return f"<Product {self.name}>"


# Category Model
# This class represents the categories of products that we're selling.
# This is a many to many relationship between products and categories.
# Two categories Genesis and Elite but some products are in both categories as it is the first of the lineup.
class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    product_categories = db.relationship(
        "ProductCategory", back_populates="category", cascade="all, delete-orphan"
    )

    products = association_proxy("product_categories", "product")

    def __repr__(self):
        return f"<Category {self.name}>"


# ProductCategory Model
# This class represents the relationship between products and categories.
# This is a many to many relationship between products and categories.
class ProductCategory(db.Model, SerializerMixin):
    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    product = db.relationship("Product", back_populates="product_categories")
    category = db.relationship("Category", back_populates="product_categories")

    def __repr__(self):
        return f"<ProductCategory Product: {self.product_id}, Category: {self.category_id}>"


# User Model
# This class represents the users of our site. They can buy products.
# Each user has an ID, username, email, and shipping address.
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    SimplePassword = db.Column(db.String(255), nullable=False)
    shipping_address = db.Column(db.Text)
    shipping_city = db.Column(db.String(255))
    shipping_state = db.Column(db.String(255))
    shipping_zip = db.Column(db.String(255))

    orders = db.relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"


# Order Model
# Represents an order made by a user. An order can contain multiple products.
class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="orders")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    order_details = db.relationship("OrderDetail", back_populates="order")

    def __repr__(self):
        return f"<Order {self.id}>"


# OrderDetail Model
# Links orders to products and includes the quantity of each product in an order.
class OrderDetail(db.Model, SerializerMixin):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    order = db.relationship("Order", back_populates="order_details")
    product = db.relationship("Product")  # this is the product object we are linking to

    def __repr__(self):
        return f"<OrderDetail Order: {self.order_id}, Product: {self.product_id}>"
