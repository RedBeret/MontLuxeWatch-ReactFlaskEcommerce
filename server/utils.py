# utils.py
from flask import jsonify
from models import Category, db
from sqlalchemy.exc import IntegrityError


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
