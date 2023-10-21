from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Structure(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(30))
    increase = db.Column(db.Float)

    def __init__(self, description, increase):
        self.description = description
        self.increase = increase


# Supplier Schema
class StructureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Structure
        sqla_session = db.session


# Init schema
structure_schema = StructureSchema()
