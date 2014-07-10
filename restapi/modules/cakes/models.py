__author__ = 'haukurk'

from restapi.modules.base import BaseModel, db
from marshmallow import Serializer, fields


class Cake(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    cakename = db.Column(db.String(80), unique=True)
    bakername = db.Column(db.String(120), unique=False)
    price = db.Column(db.Float)

    def __init__(self, cakename, bakername, price):
        self.cakename = cakename
        self.bakername = bakername
        self.price = price

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Cake %r>' % self.cakename


class CakeSerializer(Serializer):
    price_range = fields.Method("format_price_range")

    @staticmethod
    def format_price_range(cake):
        if cake.price > 100:
            return "expensive"
        return "cheap"

    class Meta:
        fields = ('id', 'cakename', 'bakername', 'price', "price_range", )