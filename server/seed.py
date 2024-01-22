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


def create_fake_users(num_users=10):
    for x in range(num_users):
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
        )
        user.password = fake_password

        db.session.add(user)

    try:
        db.session.commit()
        print(f"Added {num_users} fake users.")
    except Exception as e:
        print(f"Error adding users: {e}")


def add_product_to_categories(product, category_names):
    for name in category_names:
        category = get_or_create_category(name)
        product_category = ProductCategory(product=product, category=category)
        db.session.add(product_category)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_fake_users()

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
