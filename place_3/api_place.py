#!/usr/bin/python3
"""API pour la gestion des lieux."""

from flask import Flask
from flask_restx import Api, Resource, fields
from model_place import Place
from persistence_place import PlaceRepository
from data_manager import PlaceDataManager

app = Flask(__name__)
api = Api(app)

# Initialisation du référentiel de lieux
place_repo = PlaceRepository()
place_data_manager = PlaceDataManager(place_repo)

# Modèle de données pour la création d'un lieu
place_model = api.model('Place', {
    'name': fields.String(required=True, description='Nom du lieu'),
    'description': fields.String(description='Description du lieu'),
    'address': fields.String(description='Adresse du lieu'),
    'city_id': fields.Integer(description='ID de la ville'),
    'latitude': fields.Float(description='Latitude'),
    'longitude': fields.Float(description='Longitude'),
    'host_id': fields.Integer(description='ID de l\'hôte'),
    'number_of_rooms': fields.Integer(description='Nombre de chambres'),
    'number_of_bathrooms': fields.Integer(description='Nombre de salles de bains'),
    'price_per_night': fields.Float(description='Prix par nuit'),
    'max_guests': fields.Integer(description='Nombre maximum d\'invités'),
    'amenity_ids': fields.List(fields.String, description='Liste d\'identifiants d\'équipements')
})

@api.route('/places')
class Places(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """Récupère tous les lieux."""
        all_places = place_data_manager.get_all_places()
        return all_places

    @api.expect(place_model)
    @api.response(201, 'Lieu créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouveau lieu."""
        new_place_data = api.payload
        place_id = place_data_manager.create_place(new_place_data)
        response_message = {'message': 'Lieu créé avec succès', 'place_id': place_id}
        return response_message, 201

@api.route('/places/<int:place_id>')
class Place(Resource):
    @api.marshal_with(place_model)
    @api.response(404, 'Lieu non trouvé')
    def get(self, place_id):
        """Récupère un lieu par son identifiant."""
        place_data = place_data_manager.get_place(place_id)
        if place_data:
            return place_data
        else:
            api.abort(404, "Lieu non trouvé")

    @api.response(204, 'Lieu supprimé avec succès')
    @api.response(404, 'Lieu non trouvé')
    def delete(self, place_id):
        """Supprime un lieu existant."""
        deleted = place_data_manager.delete_place(place_id)
        if deleted:
            return {'message': 'Lieu supprimé avec succès'}, 204
        else:
            api.abort(404, "Lieu non trouvé")

    @api.expect(place_model)
    @api.response(204, 'Lieu mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Lieu non trouvé')
    def put(self, place_id):
        """Met à jour un lieu existant."""
        new_place_data = api.payload
        updated = place_data_manager.update_place(place_id, new_place_data)
        if updated:
            return {'message': 'Lieu mis à jour avec succès'}, 204
        else:
            api.abort(404, "Lieu non trouvé")

if __name__ == "__main__":
    app.run(debug=True)
