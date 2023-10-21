from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class EventModel(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    closed_space = db.Column(db.Boolean)
    format = db.Column(db.String)
    increase = db.Column(db.String)

    def __init__(self, closed_space, format, increase):
        self.closed_space = closed_space
        self.format = format
        self.increase = increase


# Schema
class EventModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventModel
        sqla_session = db.session


# Init schema
event_model_schema = EventModelSchema()
