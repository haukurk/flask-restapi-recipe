__author__ = 'haukurk'

from restapi.modules.base import BaseModel, db
from marshmallow import Serializer, fields


class Cake(BaseModel):
    """
    Cake class that defines how cake object are kept in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    cakename = db.Column(db.String(80), unique=True)
    bakername = db.Column(db.String(120), unique=False)
    price = db.Column(db.Float)

    def __init__(self, cakename, bakername, price):
        self.cakename = cakename
        self.bakername = bakername
        self.price = price

    def as_dict(self):
        #return {c.name: getattr(self, c.name) for c in self.__table__.columns} # Python 2.6 does not support this.
        cake_dict = {}
        for c in self.__table__.columns:
            cake_dict[c.name] = getattr(self, c.name)
        return cake_dict

    def __repr__(self):
        return '<Cake %r>' % self.cakename


class CakeSerializer(Serializer):
    """
    Serializer for the SQLALchemy class. The magic is performed with marshmallow module.
    """
    price_range = fields.Method("format_price_range")

    @staticmethod
    def format_price_range(cake):
        if cake.price > 100:
            return "expensive"
        return "cheap"

    class Meta:
        fields = ('id', 'cakename', 'bakername', 'price', "price_range", )