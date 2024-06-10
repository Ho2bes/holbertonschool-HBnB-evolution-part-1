#!/usr/bin/python3
"""API pour la gestion des lieux, utilisateurs, avis, équipements, pays et villes."""

from flask import Flask, request
from flask_restx import Api, Resource, fields
from data_manager import DataManager

app = Flask(__name__)
api = Api(app)

data_manager = DataManager()

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

# Modèle de données pour la création d'un utilisateur
user_model = api.model('User', {
    'username': fields.String(required=True, description='Nom d\'utilisateur'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Mot de passe')
})

# Modèle de données pour la création d'un avis
review_model = api.model('Review', {
    'user_id': fields.Integer(required=True, description='ID de l\'utilisateur'),
    'place_id': fields.Integer(required=True, description='ID du lieu'),
    'rating': fields.Integer(required=True, description='Note'),
    'comment': fields.String(description='Commentaire')
})

# Modèle de données pour la création d'un équipement
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Nom de l\'équipement')
})

# Modèle de données pour la création d'un pays
country_model = api.model('Country', {
    'name': fields.String(required=True, description='Nom du pays')
})

# Modèle de données pour la création d'une ville
city_model = api.model('City', {
    'name': fields.String(required=True, description='Nom de la ville'),
    'country_id': fields.Integer(description='ID du pays', required=True)
})

# Routes pour les lieux
@api.route('/places')
class Places(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """Récupère tous les lieux."""
        all_places = data_manager.get_all_places()
        return all_places

    @api.expect(place_model)
    @api.response(201, 'Lieu créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouveau lieu."""
        new_place_data = request.json
        place_id = data_manager.save_place(new_place_data)
        response_message = {'message': 'Lieu créé avec succès', 'place_id': place_id}
        return response_message, 201

@api.route('/places/<int:place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    @api.response(404, 'Lieu non trouvé')
    def get(self, place_id):
        """Récupère un lieu par son identifiant."""
        place_data = data_manager.get_place(place_id)
        if place_data:
            return place_data
        else:
            api.abort(404, "Lieu non trouvé")

    @api.response(204, 'Lieu supprimé avec succès')
    @api.response(404, 'Lieu non trouvé')
    def delete(self, place_id):
        """Supprime un lieu existant."""
        deleted = data_manager.delete_place(place_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Lieu non trouvé")

    @api.expect(place_model)
    @api.response(204, 'Lieu mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Lieu non trouvé')
    def put(self, place_id):
        """Met à jour un lieu existant."""
        new_place_data = request.json
        updated = data_manager.update_place(place_id, new_place_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Lieu non trouvé")

# Routes pour les utilisateurs
@api.route('/users')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Récupère tous les utilisateurs."""
        all_users = data_manager.get_all_users()
        return all_users

    @api.expect(user_model)
    @api.response(201, 'Utilisateur créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouvel utilisateur."""
        new_user_data = request.json
        user_id = data_manager.save_user(new_user_data)
        response_message = {'message': 'Utilisateur créé avec succès', 'user_id': user_id}
        return response_message, 201

@api.route('/users/<int:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    @api.response(404, 'Utilisateur non trouvé')
    def get(self, user_id):
        """Récupère un utilisateur par son identifiant."""
        user_data = data_manager.get_user(user_id)
        if user_data:
            return user_data
        else:
            api.abort(404, "Utilisateur non trouvé")

    @api.response(204, 'Utilisateur supprimé avec succès')
    @api.response(404, 'Utilisateur non trouvé')
    def delete(self, user_id):
        """Supprime un utilisateur existant."""
        deleted = data_manager.delete_user(user_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Utilisateur non trouvé")

    @api.expect(user_model)
    @api.response(204, 'Utilisateur mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Utilisateur non trouvé')
    def put(self, user_id):
        """Met à jour un utilisateur existant."""
        new_user_data = request.json
        updated = data_manager.update_user(user_id, new_user_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Utilisateur non trouvé")

# Routes pour les avis
@api.route('/reviews')
class Reviews(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Récupère tous les avis."""
        all_reviews = data_manager.get_all_reviews()
        return all_reviews

    @api.expect(review_model)
    @api.response(201, 'Avis créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouvel avis."""
        new_review_data = request.json
        review_id = data_manager.save_review(new_review_data)
        response_message = {'message': 'Avis créé avec succès', 'review_id': review_id}
        return response_message, 201

@api.route('/reviews/<int:review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    @api.response(404, 'Avis non trouvé')
    def get(self, review_id):
        """Récupère un avis par son identifiant."""
        review_data = data_manager.get_review(review_id)
        if review_data:
            return review_data
        else:
            api.abort(404, "Avis non trouvé")

    @api.response(204, 'Avis supprimé avec succès')
    @api.response(404, 'Avis non trouvé')
    def delete(self, review_id):
        """Supprime un avis existant."""
        deleted = data_manager.delete_review(review_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Avis non trouvé")

    @api.expect(review_model)
    @api.response(204, 'Avis mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Avis non trouvé')
    def put(self, review_id):
        """Met à jour un avis existant."""
        new_review_data = request.json
        updated = data_manager.update_review(review_id, new_review_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Avis non trouvé")

# Routes pour les équipements
@api.route('/amenities')
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

@api.route('/amenities/<int:amenity_id>')
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

# Routes pour les pays
@api.route('/countries')
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

@api.route('/countries/<int:country_id>')
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

# Routes pour les villes
@api.route('/cities')
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

@api.route('/cities/<int:city_id>')
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

if __name__ == "__main__":
    app.run(debug=True)

