from flask import request, jsonify

from src.app.config.config import db
from src.app.model import client_model


# Create a Quotation
def add_client():
    cnpj = request.json['cnpj']
    email = request.json['email']
    password = request.json['password']
    anual_revenue = request.json['anual_revenue']
    phone = request.json['phone']
    contact_name = request.json['contact_name']

    new_client = client_model.Client(cnpj, email, password, anual_revenue, phone, contact_name)
    db.session.add(new_client)
    db.session.commit()

    return client_model.client_schema.jsonify(new_client)


# Get All Quotations
def get_client():
    all_structure = client_model.Client.query.all()
    result = client_model.client_schema.dump(all_structure)
    return jsonify(result)


# Get Single Quotation
def get_single_client(id):
    client = client_model.Client.query.get(id)
    return client_model.client_schema.jsonify(client)


# Update a Quotation
def update_client(id):
    client = client_model.Client.query.get(id)

    client.cnpj = request.json['cnpj']
    client.email = request.json['email']
    client.password = request.json['password']
    client.anual_revenue = request.json['anual_revenue']
    client.phone = request.json['phone']
    client.contact_name = request.json['contact_name']

    db.session.commit()

    return client_model.client_schema.jsonify(client_model)


# Delete Quotation
def delete_client(id):
    client = client_model.Client.query.get(id)
    db.session.delete(client)
    db.session.commit()

    return client.client_schema.jsonify(client)
