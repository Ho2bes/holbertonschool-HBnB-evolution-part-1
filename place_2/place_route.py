#!/usr/bin/python3

from flask import Flask, jsonify, request
from persistence_place import PlaceRepository

app = Flask(__name__)
place_repo = PlaceRepository()

@app.route('/places', methods=['GET'])
def get_places():
    """Route pour récupérer tous les lieux."""
    all_places = place_repo.get_all_places()
    return jsonify(all_places)

@app.route('/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    """Route pour récupérer un lieu par son identifiant."""
    place_data = place_repo.get_place(place_id)
    if place_data:
        return jsonify(place_data)
    else:
        return jsonify({'error': 'Place not found'}), 404

@app.route('/places', methods=['POST'])
def create_place():
    """Route pour créer un nouveau lieu."""
    new_place_data = request.json
    place_id = place_repo.create_place(new_place_data)
    return jsonify({'message': 'Lieu créé avec succès', 'place_id': place_id}), 201

@app.route('/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    """Route pour mettre à jour un lieu existant."""
    new_place_data = request.json
    success = place_repo.update_place(place_id, new_place_data)
    if success:
        return jsonify({'message': 'Lieu mis à jour avec succès'})
    else:
        return jsonify({'error': 'Place not found'}), 404

@app.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Route pour supprimer un lieu existant."""
    success = place_repo.delete_place(place_id)
    if success:
        return jsonify({'message': 'Lieu supprimé avec succès'})
    else:
        return jsonify({'error': 'Place not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
