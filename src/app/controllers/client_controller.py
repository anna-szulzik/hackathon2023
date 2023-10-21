from flask import request, jsonify

from src.app.config.config import db
from src.app.model import client_model


# Create a Quotation
def add_structure():
    description = request.json['description']
    increase = request.json['increase']

    new_structure = client_model.Client(description, increase)
    db.session.add(new_structure)
    db.session.commit()

    return client_model.client_schema.jsonify(new_structure)


# Get All Quotations
def get_structure():
    all_structure = client_model.Client.query.all()
    result = client_model.client_schema.dump(all_structure)
    return jsonify(result)


# Get Single Quotation
def get_single_structure(id):
    client = client_model.Structure.query.get(id)
    return client_model.structure_schema.jsonify(client)


# Update a Quotation
def update_structure(id):
    structure = client_model.Client.query.get(id)

    description = request.json['description']
    increase = request.json['increase']

    structure.description = description
    structure.cost = increase

    db.session.commit()

    return client_model.client_schema.jsonify(client_model)


# Delete Quotation
def delete_structure(id):
    client = client_model.Client.query.get(id)
    db.session.delete(client)
    db.session.commit()

    return client.structure_schema.jsonify(client)
