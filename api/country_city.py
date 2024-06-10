#!/usr/bin/python3
"""API pour la gestion des pays et des villes."""

from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace
from model.country import Country
from model.city import City
from persistence.data_manager import CityRepository

api = Namespace('countries_cities', description='API pour la gestion des pays et des villes')

# Initialisation du référentiel de villes
city_repo = CityRepository()

# Pré-chargement des pays
countries = [
    Country('US', 'United States'),
    Country('FR', 'France'),
    Country('ES', 'Spain'),
    # Ajoutez d'autres pays ici
]

# Modèle de données pour la création d'une ville
city_model = api.model('City', {
    'name': fields.String(required=True, description='Nom de la ville'),
    'country_code': fields.String(required=True, description='Code du pays')
})

@api.route('/countries')
class Countries(Resource):
    def get(self):
        """Récupère tous les pays."""
        return [{'code': country.code, 'name': country.name} for country in countries]

@api.route('/countries/<string:country_code>')
class CountryResource(Resource):
    def get(self, country_code):
        """Récupère un pays par son code."""
        country = next((country for country in countries if country.code == country_code), None)
        if country:
            return {'code': country.code, 'name': country.name}
        else:
            api.abort(404, "Pays non trouvé")

@api.route('/countries/<string:country_code>/cities')
class CountryCities(Resource):
    @api.marshal_list_with(city_model)
    def get(self, country_code):
        """Récupère toutes les villes d'un pays."""
        all_cities = [city for city in city_repo.get_all() if city.country_code == country_code]
        return all_cities

@api.route('/cities')
class Cities(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        """Récupère toutes les villes."""
        all_cities = city_repo.get_all()
        return all_cities

    @api.expect(city_model)
    @api.response(201, 'Ville créée avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(409, 'Conflit : nom de ville déjà existant dans le pays')
    def post(self):
        """Crée une nouvelle ville."""
        new_city_data = request.json
        if not all(key in new_city_data for key in ('name', 'country_code')):
            api.abort(400, 'Les champs name et country_code sont requis.')
        if not any(country.code == new_city_data['country_code'] for country in countries):
            api.abort(400, 'Code du pays invalide.')
        if not city_repo.is_name_unique(new_city_data['name'], new_city_data['country_code']):
            api.abort(409, 'Le nom de la ville existe déjà dans ce pays.')
        city_id = city_repo.create(new_city_data)
        response_message = {'message': 'Ville créée avec succès', 'city_id': city_id}
        return response_message, 201

@api.route('/cities/<string:city_id>')
class CityResource(Resource):
    @api.marshal_with(city_model)
    @api.response(404, 'Ville non trouvée')
    def get(self, city_id):
        """Récupère une ville par son identifiant."""
        city_data = city_repo.get(city_id)
        if city_data:
            return city_data
        else:
            api.abort(404, "Ville non trouvée")

    @api.response(204, 'Ville supprimée avec succès')
    @api.response(404, 'Ville non trouvée')
    def delete(self, city_id):
        """Supprime une ville existante."""
        deleted = city_repo.delete(city_id)
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
        if not all(key in new_city_data for key in ('name', 'country_code')):
            api.abort(400, 'Les champs name et country_code sont requis.')
        updated = city_repo.update(city_id, new_city_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Ville non trouvée")
