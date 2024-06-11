#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask import request
from persistence.data_manager import DataManager

data_manager = DataManager()

api = Namespace('cities', description='Opérations liées aux villes')

# Modèle de données pour la création d'une ville
city_model = api.model('City', {
    'name': fields.String(required=True, description='Nom de la ville'),
    'country_id': fields.Integer(description='ID du pays', required=True)
})

@api.route('/')
class Cities(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        """Récupère toutes les villes."""
        all_cities = data_manager.get_all_cities()
        return all_cities

    @api.expect(city_model)
    @api.response(201, 'Ville créée avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée une nouvelle ville."""
        new_city_data = request.json
        city_id = data_manager.save_city(new_city_data)
        response_message = {'message': 'Ville créée avec succès', 'city_id': city_id}
        return response_message, 201

@api.route('/<int:city_id>')
class CityResource(Resource):
    @api.marshal_with(city_model)
    @api.response(404, 'Ville non trouvée')
    def get(self, city_id):
        """Récupère une ville par son identifiant."""
        city_data = data_manager.get_city(city_id)
        if city_data:
            return city_data
        else:
            api.abort(404, "Ville non trouvée")

    @api.response(204, 'Ville supprimée avec succès')
    @api.response(404, 'Ville non trouvée')
    def delete(self, city_id):
        """Supprime une ville existante."""
        deleted = data_manager.delete_city(city_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Ville non trouvée")

    @api.expect(city_model)
    @api.response(204, 'Ville mise à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Ville non trouvée')
    def put(self, city_id):
        """Met à jour une ville existante."""
        new_city_data = request.json
        updated = data_manager.update_city(city_id, new_city_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Ville non trouvée")
