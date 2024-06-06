#!/usr/bin/python3
"""API pour la gestion des lieux."""

from flask import Flask, jsonify, request
from model_place import Place
from persistence_place import PlaceRepository
from place_route import app

app = Flask(__name__)
place_repo = PlaceRepository()

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Récupère un lieu par son identifiant."""
    place_data = place_repo.get_place(place_id)
    if place_data:
        return jsonify(place_data)
    else:
        return jsonify({'error': 'Lieu non trouvé'}), 404

# D'autres routes pour les opérations CRUD peuvent être ajoutées ici

if __name__ == "__main__":
    app.run(debug=True)
