from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Quotation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer)
    event_type = db.Column(db.Integer)
    event_model = db.Column(db.Integer)
    event_suppliers = db.Column(db.Integer)
    venue = db.Column(db.Integer)
    structure = db.Column(db.Integer)
    service = db.Column(db.Integer)
    custom_decoration = db.Column(db.Boolean)
    custom_prints = db.Column(db.Boolean)
    marketing = db.Column(db.Boolean)
    init_time = db.Column(db.String(20))
    end_time = db.Column(db.String(20))

    def __init__(self, client_id, event_type, event_model, event_suppliers, venue, structure, service,
                 custom_decoration, custom_prints, marketing, init_time, end_time):
        self.client_id = client_id
        self.event_type = event_type
        self.event_model = event_model
        self.event_suppliers = event_suppliers
        self.venue = venue
        self.structure = structure
        self.service = service
        self.custom_decoration = custom_decoration
        self.custom_prints = custom_prints
        self.marketing = marketing
        self.init_time = init_time
        self.end_time = end_time


# Quotation Schema
class QuotationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quotation
        sqla_session = db.session


# Init schema
quotation_schema = QuotationSchema()
