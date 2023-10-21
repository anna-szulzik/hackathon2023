from flask import request, jsonify

from src.app.config.config import db
from src.app.model import venue_model


# Create a Venue
def add_venue():
    maximum_capacity = request.json['maximum_capacity']
    minimum_capacity = request.json['minimum_capacity']
    nome = request.json['nome']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    closed_space = request.json['closed_space']
    cost = request.json['cost']

    new_product = venue_model.Venue(maximum_capacity, minimum_capacity, nome, latitude, longitude, closed_space, cost)

    db.session.add(new_product)
    db.session.commit()

    return venue_model.venue_schema.jsonify(new_product)


# Get All Venues
def get_venues():
    all_venues = venue_model.Venue.query.all()
    result = venue_model.venue_schema.dump(all_venues)
    return jsonify(result)


# Get Single Venue
def get_venue(id):
    product = venue_model.Venue.query.get(id)
    return venue_model.venue_schema.jsonify(product)


# Update a Venue
def update_venue(id):
    venue = venue_model.Venue.query.get(id)

    maximum_capacity = request.json['maximum_capacity']
    minimum_capacity = request.json['minimum_capacity']
    nome = request.json['nome']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    closed_space = request.json['closed_space']
    cost = request.json['cost']

    venue.maximum_capacity = maximum_capacity
    venue.minimum_capacity = minimum_capacity
    venue.nome = nome
    venue.latitude = latitude
    venue.longitude = longitude
    venue.closed_space = closed_space
    venue.cost = cost

    db.session.commit()

    return venue_model.venue_schema.jsonify(venue)


# Delete Venue
def delete_product(id):
    product = venue_model.Venue.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return venue_model.venue_schema.jsonify(product)
