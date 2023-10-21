from flask import request, jsonify

from src.app.config.config import db
from src.app.model import event_type_model


# Create a Quotation
def add_event_type():
    description = request.json['description']
    increase = request.json['increase']

    new_event_type = event_type_model.EventType(description, increase)

    db.session.add(new_event_type)
    db.session.commit()

    return event_type_model.event_type_schema.jsonify(new_event_type)


# Get All Quotations
def get_event_type():
    all_event_type = event_type_model.EventType.query.all()
    result = event_type_model.event_type_schema.dump(all_event_type)
    return jsonify(result)


# Get Single Event Type
def get_single_event_type(id):
    event_type = event_type_model.EventType.query.get(id)
    return event_type_model.event_type_schema.jsonify(event_type)


# Update a Quotation
def update_event_type(id):
    event_type = event_type_model.EventType.query.get(id)

    description = request.json['description']
    increase = request.json['increase']

    event_type.description = description
    event_type.cost = increase

    db.session.commit()

    return event_type_model.event_type_schema.jsonify(event_type)


# Delete Quotation
def delete_event_type(id):
    event_type = event_type_model.EventType.query.get(id)
    db.session.delete(event_type)
    db.session.commit()

    return event_type.event_type_schema.jsonify(event_type)