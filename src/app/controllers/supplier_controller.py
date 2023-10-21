from flask import request, jsonify

from src.app.config.config import db
from src.app.model import supplier_model


# Create a Quotation
def add_supplier():
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    seguimento = request.json['seguimento']
    name = request.json['name']
    cost = request.json['cost']

    new_supplier = supplier_model.Supplier(name, latitude, longitude, cost, seguimento)

    db.session.add(new_supplier)
    db.session.commit()

    return supplier_model.supplier_schema.jsonify(new_supplier)


# Get All Quotations
def get_supplier():
    all_supplier = supplier_model.Supplier.query.all()
    result = supplier_model.supplier_schema.dump(all_supplier)
    return jsonify(result)


# Get Single Quotation
def get_single_supplier(id):
    supplier = supplier_model.Supplier.query.get(id)
    return supplier_model.supplier_schema.jsonify(supplier)


# Update a Quotation
def update_supplier(id):
    supplier = supplier_model.Supplier.query.get(id)

    latitude = request.json['latitude']
    longitude = request.json['longitude']
    seguimento = request.json['seguimento']
    nome = request.json['nome']
    custo = request.json['custo']

    supplier.latitude = latitude
    supplier.longitude = longitude
    supplier.seguimento = seguimento
    supplier.nome = nome
    supplier.custo = custo

    db.session.commit()

    return supplier_model.supplier_schema.jsonify(supplier)


# Delete Quotation
def delete_supplier(id):
    supplier = supplier_model.Supplier.query.get(id)
    db.session.delete(supplier)
    db.session.commit()

    return supplier_model.supplier_schema.jsonify(supplier)
