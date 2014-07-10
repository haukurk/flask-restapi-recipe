__author__ = 'haukurk'

from restapi import db


class BaseModel(db.Model):
    """
    a base model for other database tables to inherit
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())