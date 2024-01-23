#!/usr/bin/env python3
# seed.py
# Standard library imports
from random import choice as rc
from random import randint

import bcrypt
from app import commit_session, get_or_create_category
from config import app, db
from faker import Faker
from flask_bcrypt import Bcrypt
from models import Category, Order, OrderDetail, Product, ProductCategory, User
from sqlalchemy.exc import IntegrityError, NoResultFound

products_data = [
    {
        "name": "Alpine Elegance",
        "imageSrc": "assets/images/alpine_elegance.png",
        "imageAlt": "Sophisticated Alpine Elegance watch showcasing Swiss craftsmanship.",
        "category_name": "Genesis",
    },
    {
        "name": "Horologe Elegance Alpine",
        "imageSrc": "assets/images/horologe_elegance_alpine.png",
        "imageAlt": "The Horologe Elegance Alpine watch blends tradition with alpine scenery.",
        "category_name": "Elite",
    },
    {
        "name": "Pastoral Reflection",
        "imageSrc": "assets/images/pastoral_reflection.png",
        "imageAlt": "The Pastoral Reflection watch, where time meets the tranquility of nature.",
        "category_name": "Genesis",
    },
    {
        "name": "Urban Allegory",
        "imageSrc": "assets/images/urban_allegory.png",
        "imageAlt": "Urban Allegory, a watch that embodies the spirit of the metropolis.",
        "category_name": "Elite",
    },
    {
        "name": "Haute Society",
        "imageSrc": "assets/images/haute_society.png",
        "imageAlt": "Haute Society, the watch that epitomizes the zenith of luxury.",
        "category_name": "Genesis",
    },
    {
        "name": "Alpine Precision",
        "imageSrc": "assets/images/alpine_precision.png",
        "imageAlt": "Alpine Precision, a watch that defines accuracy and Swiss elegance.",
        "category_name": "Elite",
    },
    {
        "name": "Alpine Enforcer",
        "imageSrc": "assets/images/alpine_enforcer.png",
        "imageAlt": "The Alpine Enforcer watch, robustness and precision in one piece.",
        "category_name": ["Genesis", "Elite"],
    },
    {
        "name": "Urban Reflection",
        "imageSrc": "assets/images/urban_reflection.png",
        "imageAlt": "Urban Reflection, the essence of city life on your wrist.",
        "category_name": ["Genesis", "Elite"],
    },
    {
        "name": "Velocity Visionary",
        "imageSrc": "assets/images/velocity_visionary.png",
        "imageAlt": "Velocity Visionary, where speed and vision meet sophistication.",
        "category_name": ["Genesis", "Elite"],
    },
]

fake = Faker()
bcrypt = Bcrypt(app)


def create_fake_orders(num_orders=5):
    for _ in range(num_orders):
        user_id = rc(User.query.all()).id
        order = Order(user_id=user_id)
        db.session.add(order)

    try:
        db.session.commit()
        print(f"Added {num_orders} fake orders.")
    except Exception as e:
        print(f"Error adding orders: {e}")


def create_fake_order_details(num_details=10):
    products = Product.query.all()
    if not products:
        print("No products available to create order details.")
        return

    for _ in range(num_details):
        order_id = rc(Order.query.all()).id
        product_id = rc(products).id
        quantity = randint(1, 5)

        order_detail = OrderDetail(
            order_id=order_id, product_id=product_id, quantity=quantity
        )
        db.session.add(order_detail)

    try:
        db.session.commit()
        print(f"Added {num_details} fake order details.")
    except Exception as e:
        print(f"Error adding order details: {e}")


def create_fake_users(num_users=10):
    for x in range(num_users):
        try:
            username = fake.user_name()
            email = fake.email()

            existing_user = User.query.filter(
                (User.username == username) | (User.email == email)
            ).first()
            if existing_user:
                print(f"User '{username}' or email '{email}' already exists. Skipping.")
                continue
            fake_password = fake.password()

            user = User(
                username=username,
                email=email,
                shipping_address=fake.address(),
                shipping_city=fake.city(),
                shipping_state=fake.state(),
                shipping_zip=fake.zipcode(),
                password=fake_password,  # Set the password here
            )

            db.session.add(user)
            db.session.commit()
            print(f"Added user: {user.username}")

        except Exception as e:
            print(f"Error adding user {username}: {e}")
            db.session.rollback()


def add_product_to_categories(product, category_names):
    for name in category_names:
        category = get_or_create_category(name)
        product_category = ProductCategory(product=product, category=category)
        db.session.add(product_category)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_fake_users()
        create_fake_orders()
        create_fake_order_details()

        for product_data in products_data:
            try:
                existing_product = Product.query.filter_by(
                    name=product_data["name"]
                ).one()
                print(f"Product '{existing_product.name}' already exists. Skipping.")
            except NoResultFound:
                product = Product(
                    name=product_data["name"],
                    description=fake.text(),
                    price=fake.random_int(min=30000, max=160000),
                    item_quantity=fake.random_int(min=0, max=100),
                    image_url=f"assets/images/{product_data['imageSrc']}",
                    imageAlt=product_data["imageAlt"],
                )

                category_names = (
                    product_data["category_name"]
                    if isinstance(product_data["category_name"], list)
                    else [product_data["category_name"]]
                )
                add_product_to_categories(product, category_names)

                db.session.add(product)
                try:
                    commit_session(db.session)
                except IntegrityError as error:
                    print(f"Failed to add product: {product.name}. Error: {error}")

        print("Database seeded successfully!")
