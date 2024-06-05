#!/usr/bin/python3
""" code for api class place"""


from flask import Flask, jsonify, request
from model.place import Place
from persistence.place_repository import PlaceRepository

app = Flask(__name__)
place_repo = PlaceRepository()

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Route pour récupérer un lieu par son identifiant."""
    place_data = place_repo.get_place(place_id)
    if place_data:
        return jsonify(place_data)
    else:
        return jsonify({'error': 'Place not found'}), 404

# D'autres routes pour les opérations CRUD peuvent être ajoutées ici
