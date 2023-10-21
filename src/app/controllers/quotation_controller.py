from flask import request, jsonify
import json

from src.app.config.config import db
from src.app.model import quotation_model, event_type_model, service_model, supplier_model, venue_model, \
    structure_model, event_model_model


# Add new Quotation
def add_quotation():
    client_id = request.json['client_id']
    event_type = request.json['event_type']
    event_model = request.json['event_model']
    event_suppliers = request.json['event_suppliers']
    venue = request.json['venue']
    structure = request.json['structure']
    service = request.json['service']
    custom_decoration = request.json['custom_decoration']
    custom_prints = request.json['custom_prints']
    marketing = request.json['marketing']
    init_time = request.json['init_time']
    end_time = request.json['end_time']

    new_quotation = quotation_model.Quotation(client_id, event_type, event_model, event_suppliers, venue, structure,
                                              service, custom_decoration, custom_prints, marketing, init_time, end_time)

    db.session.add(new_quotation)
    db.session.commit()

    return quotation_model.quotation_schema.jsonify(new_quotation)


def get_quotation_data(quotation):
    event_type = event_type_model.EventType.query.get(quotation.event_type)
    event_model = event_model_model.EventModel.query.get(quotation.event_model)
    service = service_model.Service.query.get(quotation.event_model)
    event_suppliers = supplier_model.Supplier.query.get(quotation.event_suppliers)
    venue = venue_model.Venue.query.get(quotation.venue)
    structure = structure_model.Structure.query.get(quotation.structure)

    quotation_data = {
        'id': quotation.id,
        'client_id': quotation.client_id,
        'event_type': {
            'description': event_type.description if event_type else None,
            'cost': event_type.cost if event_type else None
        },
        'event_model': {
            'closed_space': event_model.closed_space if event_model else None,
            'format': event_model.format if event_model else None,
            'increase': event_model.increase if event_model else None
        },
        'event_suppliers': {
            'name': event_suppliers.name if event_suppliers else None,
            'type': event_suppliers.type if event_suppliers else None,
            'latitude': event_suppliers.latitude if event_suppliers else None,
            'longitude': event_suppliers.longitude if event_suppliers else None,
            'cost_increase': event_suppliers.cost_increase if event_suppliers else None
        },
        'venue': {
            'name': venue.name if venue else None,
            'maximum_capacity': venue.maximum_capacity if venue else None,
            'minimum_capacity': venue.minimum_capacity if venue else None,
            'latitude': venue.latitude if venue else None,
            'longitude': venue.longitude if venue else None,
            'cost': venue.cost if venue else None
        },
        'structure': {
            'description': structure.description if structure else None,
            'increase': structure.increase if structure else None
        },
        'service': {
            'description': service.description if service else None,
            'cost': service.cost if service else None
        },
        'custom_decoration': quotation.custom_decoration,
        'custom_prints': quotation.custom_prints,
        'marketing': quotation.marketing,
        'init_time': quotation.init_time,
        'end_time': quotation.end_time
    }
    return quotation_data


# Get Single Quotation
def get_quotation(id):
    quotation = quotation_model.Quotation.query.get(id)
    if quotation is None:
        return json.dumps({'error': 'Quotation not found'})
    return json.dumps(get_quotation_data(quotation))


# Get All Quotations
def get_all_quotations():
    quotations = quotation_model.Quotation.query.all()
    quotations_data = [get_quotation_data(quotation) for quotation in quotations]
    return json.dumps(quotations_data)


# Get All Quotations from a Client
def get_all_quotations_from_client(client_id):
    quotations = quotation_model.Quotation.query.filter_by(client_id=client_id).all()
    quotations_data = [get_quotation_data(quotation) for quotation in quotations]
    return json.dumps(quotations_data)


# Update a Quotation
def update_quotation(id):
    quotation = quotation_model.Quotation.query.get(id)

    quotation.client_id = request.json['client_id']
    quotation.event_type = request.json['event_type']
    quotation.event_model = request.json['event_model']
    quotation.event_suppliers = request.json['event_suppliers']
    quotation.venue = request.json['venue']
    quotation.structure = request.json['structure']
    quotation.service = request.json['service']
    quotation.custom_decoration = request.json['custom_decoration']
    quotation.custom_prints = request.json['custom_prints']
    quotation.marketing = request.json['marketing']
    quotation.init_time = request.json['init_time']
    quotation. end_time = request.json['end_time']

    db.session.commit()

    return quotation_model.quotation_schema.jsonify(quotation)


# Delete Quotation
def delete_quotation(id):
    quotation = quotation_model.Quotation.query.get(id)
    db.session.delete(quotation)
    db.session.commit()

    return quotation_model.quotation_schema.jsonify(quotation)


# Get Quotations By Client
def get_quotations_by_client(client_id):
    client_quotations = quotation_model.Quotation.query.filter_by(client_id=client_id).all()
    result = quotation_model.quotation_schema.dump(client_quotations)
    return jsonify(result)