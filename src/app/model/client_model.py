from sqlalchemy.ext.declarative import declarative_base
from src.app.config.config import db, ma

Base = declarative_base()


class Client(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    cnpj = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)

    CNPJ

    EMAIL
    EMPRESARIAL
    SENHA
    FATURAMENTO
    TELEFONE(CONTATO)
    NOME(CONTATO)

    def __init__(self, description, increase):
        self.description = description
        self.increase = increase


# Supplier Schema
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        sqla_session = db.session


# Init schema
structure_schema = ClientSchema()
