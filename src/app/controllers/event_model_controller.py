from flask import request, jsonify

from src.app.config.config import db
from src.app.model import event_model_model


# Create a Quotation
def add_event_model():
    closed_space = request.json['closed_space']
    format = request.json['format']
    increase = request.json['increase']

    new_event_model = event_model_model.EventModel(closed_space, format, increase)
    db.session.add(new_event_model)
    db.session.commit()

    return event_model_model.event_model_schema.jsonify(new_event_model)


# Get All Quotations
def get_event_model():
    all_event_model = event_model_model.EventModel.query.all()
    result = event_model_model.event_model_schema.dump(all_event_model)
    return jsonify(result)


# Get Single Quotation
def get_single_event_model(id):
    event_model = event_model_model.EventModel.query.get(id)
    return event_model_model.event_model_schema.jsonify(event_model)


# Update a Quotation
def update_event_model(id):
    event_model = event_model_model.EventModel.query.get(id)

    closed_space = request.json['closed_space']
    format = request.json['format']
    increase = request.json['increase']

    event_model.closed_space = closed_space
    event_model.format = format
    event_model.increase = increase

    db.session.commit()

    return event_model_model.event_model_schema.jsonify(event_model)


# Delete Quotation
def delete_event_model(id):
    event_model = event_model_model.EventModel.query.get(id)
    db.session.delete(event_model)
    db.session.commit()

    return event_model.event_model_schema.jsonify(event_model)