from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Client(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    cnpj = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    anual_revenue = db.Column(db.Float)
    phone = db.Column(db.Integer)
    contact_name = db.Column(db.String)

    def __init__(self, cnpj, email, password, anual_revenue, phone, contact_name):
        self.cnpj = cnpj
        self.email = email
        self.password = password
        self.anual_revenue = anual_revenue
        self.phone = phone
        self.contact_name = contact_name


# Supplier Schema
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        sqla_session = db.session


# Init schema
client_schema = ClientSchema()
