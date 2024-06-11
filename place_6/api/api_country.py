#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask import request
from persistence.data_manager import DataManager

data_manager = DataManager()

api = Namespace('countries', description='Opérations liées aux pays')

# Modèle de données pour la création d'un pays
country_model = api.model('Country', {
    'name': fields.String(required=True, description='Nom du pays')
})

@api.route('/')
class Countries(Resource):
    @api.marshal_list_with(country_model)
    def get(self):
        """Récupère tous les pays."""
        all_countries = data_manager.get_all_countries()
        return all_countries

    @api.expect(country_model)
    @api.response(201, 'Pays créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouveau pays."""
        new_country_data = request.json
        country_id = data_manager.save_country(new_country_data)
        response_message = {'message': 'Pays créé avec succès', 'country_id': country_id}
        return response_message, 201

@api.route('/<int:country_id>')
class CountryResource(Resource):
    @api.marshal_with(country_model)
    @api.response(404, 'Pays non trouvé')
    def get(self, country_id):
        """Récupère un pays par son identifiant."""
        country_data = data_manager.get_country(country_id)
        if country_data:
            return country_data
        else:
            api.abort(404, "Pays non trouvé")

    @api.response(204, 'Pays supprimé avec succès')
    @api.response(404, 'Pays non trouvé')
    def delete(self, country_id):
        """Supprime un pays existant."""
        deleted = data_manager.delete_country(country_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Pays non trouvé")

    @api.expect(country_model)
    @api.response(204, 'Pays mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Pays non trouvé')
    def put(self, country_id):
        """Met à jour un pays existant."""
        new_country_data = request.json
        updated = data_manager.update_country(country_id, new_country_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Pays non trouvé")

