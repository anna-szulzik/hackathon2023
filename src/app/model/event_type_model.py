from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class EventType(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(30))
    cost = db.Column(db.Float)

    def __init__(self, desc, cost):
        self.description = desc
        self.cost = cost


# Schema
class EventTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventType
        sqla_session = db.session


# Init schema
event_type_schema = EventTypeSchema()
