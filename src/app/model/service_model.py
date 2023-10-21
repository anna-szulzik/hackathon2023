from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Service(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(30))
    cost = db.Column(db.Float)

    def __init__(self, description, cost):
        self.description = description
        self.cost = cost


# Supplier Schema
class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        sqla_session = db.session


# Init schema
service_schema = ServiceSchema()
