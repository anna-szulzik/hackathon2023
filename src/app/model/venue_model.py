from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Venue(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    maximum_capacity = db.Column(db.Integer)
    minimum_capacity = db.Column(db.Integer)
    name = db.Column(db.String(30))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    closed_space = db.Column(db.Boolean)
    cost = db.Column(db.Float)

    def __init__(self, name, maximum_capacity, minimum_capacity, latitude, longitude, closed_space, cost):
        self.maximum_capacity = maximum_capacity
        self.minimum_capacity = minimum_capacity
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.closed_space = closed_space
        self.cost = cost


# Schema
class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Venue
        sqla_session = db.session


# Init schema
venue_schema = VenueSchema()
