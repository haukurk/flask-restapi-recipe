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


class APIAuth(BaseModel):
    """
    Model for APIKEYs.
    """
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), unique=True)
    ip = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(255), unique=False)

    def __init__(self, key, ip, description):
        self.key = key
        self.ip = ip
        self.description = description

    def __repr__(self):
        return '<Key %r>' % self.ip