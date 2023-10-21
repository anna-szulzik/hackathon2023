from flask import request, jsonify

from src.app.config.config import db
from src.app.model import service_model


# Create a Quotation
def add_service():
    description = request.json['description']
    cost = request.json['cost']

    new_service = service_model.Service(description, cost)
    db.session.add(new_service)
    db.session.commit()

    return service_model.service_schema.jsonify(new_service)


# Get All Quotations
def get_service():
    all_service = service_model.Service.query.all()
    result = service_model.service_schema.dump(all_service)
    return jsonify(result)


# Get Single Quotation
def get_single_service(id):
    service = service_model.Service.query.get(id)
    return service_model.service_schema.jsonify(service_model)


# Update a Quotation
def update_service(id):
    service = service_model.Service.query.get(id)

    description = request.json['description']
    cost = request.json['cost']

    service.description = description
    service.cost = cost

    db.session.commit()

    return service_model.service_schema.jsonify(service)


# Delete Quotation
def delete_service(id):
    service = service_model.Service.query.get(id)
    db.session.delete(service)
    db.session.commit()

    return service.service_schema.jsonify(service)
