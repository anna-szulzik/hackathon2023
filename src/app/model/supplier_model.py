from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Supplier(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(30))
    type = db.Column(db.String(30))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    cost_increase = db.Column(db.Float)

    def __init__(self, name, latitude, longitude, cost_increase, type):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.cost_increase = cost_increase
        self.type = type


# Supplier Schema
class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        sqla_session = db.session


# Init schema
supplier_schema = SupplierSchema()
