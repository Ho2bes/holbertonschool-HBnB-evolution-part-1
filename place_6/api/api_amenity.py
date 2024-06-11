#!/usr/bin/python3


from flask_restx import Namespace, Resource, fields
from flask import request
from persistence.data_manager import DataManager

data_manager = DataManager()

api = Namespace('amenities', description='Opérations liées aux équipements')

# Modèle de données pour la création d'un équipement
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Nom de l\'équipement')
})

@api.route('/')
class Amenities(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Récupère tous les équipements."""
        all_amenities = data_manager.get_all_amenities()
        return all_amenities

    @api.expect(amenity_model)
    @api.response(201, 'Équipement créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouvel équipement."""
        new_amenity_data = request.json
        amenity_id = data_manager.save_amenity(new_amenity_data)
        response_message = {'message': 'Équipement créé avec succès', 'amenity_id': amenity_id}
        return response_message, 201

@api.route('/<int:amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    @api.response(404, 'Équipement non trouvé')
    def get(self, amenity_id):
        """Récupère un équipement par son identifiant."""
        amenity_data = data_manager.get_amenity(amenity_id)
        if amenity_data:
            return amenity_data
        else:
            api.abort(404, "Équipement non trouvé")

    @api.response(204, 'Équipement supprimé avec succès')
    @api.response(404, 'Équipement non trouvé')
    def delete(self, amenity_id):
        """Supprime un équipement existant."""
        deleted = data_manager.delete_amenity(amenity_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Équipement non trouvé")

    @api.expect(amenity_model)
    @api.response(204, 'Équipement mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Équipement non trouvé')
    def put(self, amenity_id):
        """Met à jour un équipement existant."""
        new_amenity_data = request.json
        updated = data_manager.update_amenity(amenity_id, new_amenity_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Équipement non trouvé")
