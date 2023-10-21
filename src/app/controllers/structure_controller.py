from flask import request, jsonify

from src.app.config.config import db
from src.app.model import structure_model


# Create a Quotation
def add_structure():
    description = request.json['description']
    increase = request.json['increase']

    new_structure = structure_model.Structure(description, increase)
    db.session.add(new_structure)
    db.session.commit()

    return structure_model.structure_schema.jsonify(new_structure)


# Get All Quotations
def get_structure():
    all_structure = structure_model.Structure.query.all()
    result = structure_model.structure_schema.dump(all_structure)
    return jsonify(result)


# Get Single Quotation
def get_single_structure(id):
    structure = structure_model.Structure.query.get(id)
    return structure_model.structure_schema.jsonify(structure)


# Update a Quotation
def update_structure(id):
    structure = structure_model.Structure.query.get(id)

    description = request.json['description']
    increase = request.json['increase']

    structure.description = description
    structure.cost = increase

    db.session.commit()

    return structure_model.structure_schema.jsonify(structure_model)


# Delete Quotation
def delete_structure(id):
    structure = structure_model.Structure.query.get(id)
    db.session.delete(structure)
    db.session.commit()

    return structure.structure_schema.jsonify(structure)
