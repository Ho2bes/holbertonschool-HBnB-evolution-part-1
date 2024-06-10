#!/usr/bin/python3
"""API pour la gestion des utilisateurs."""

from flask import request
from flask_restx import Namespace, Resource, fields
from model.user import User
from persistence.data_manager import UserRepository
import uuid
from datetime import datetime, timezone

# Création du namespace et de l'API Flask-RESTx
api = Namespace('users', description='API pour la gestion des utilisateurs')

# Initialisation du référentiel d'utilisateurs
user_repo = UserRepository()

# Modèle de données pour la création d'un utilisateur
user_model = api.model('User', {
    'email': fields.String(required=True, description='Adresse e-mail de l\'utilisateur'),
    'first_name': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'last_name': fields.String(required=True, description='Nom de famille de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur')
})

@api.route('/')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Récupère tous les utilisateurs."""
        all_users = user_repo.get_all()
        return all_users

    @api.expect(user_model)
    @api.response(201, 'Utilisateur créé avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(409, 'Conflit : e-mail déjà existant')
    def post(self):
        """Crée un nouvel utilisateur."""
        new_user_data = api.payload
        # Validation des données d'entrée
        if not new_user_data.get('email') or not new_user_data.get('first_name') or not new_user_data.get('last_name') or not new_user_data.get('password'):
            api.abort(400, 'Les champs email, first_name, last_name et password sont requis.')

        if not user_repo.is_email_unique(new_user_data['email']):
            api.abort(409, 'L\'adresse e-mail existe déjà.')

        new_user_data['id'] = str(uuid.uuid4())
        new_user_data['created_at'] = datetime.now(timezone.utc).isoformat()
        new_user_data['updated_at'] = datetime.now(timezone.utc).isoformat()

        user_id = user_repo.create_user(new_user_data)
        return {'message': 'Utilisateur créé avec succès', 'user_id': user_id}, 201

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    @api.response(404, 'Utilisateur non trouvé')
    def get(self, user_id):
        """Récupère un utilisateur par son identifiant."""
        user_data = user_repo.get(user_id)
        if user_data:
            return user_data
        else:
            api.abort(404, "Utilisateur non trouvé")

    @api.response(204, 'Utilisateur supprimé avec succès')
    @api.response(404, 'Utilisateur non trouvé')
    def delete(self, user_id):
        """Supprime un utilisateur existant."""
        deleted = user_repo.delete(user_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Utilisateur non trouvé")

    @api.expect(user_model)
    @api.response(204, 'Utilisateur mis à jour avec succès')
    @api.response(400, 'Requête invalide')
    @api.response(404, 'Utilisateur non trouvé')
    @api.response(409, 'Conflit : e-mail déjà existant')
    def put(self, user_id):
        """Met à jour un utilisateur existant."""
        new_user_data = api.payload
        # Validation des données d'entrée
        if not new_user_data.get('email') or not new_user_data.get('first_name') or not new_user_data.get('last_name') or not new_user_data.get('password'):
            api.abort(400, 'Les champs email, first_name, last_name et password sont requis.')

        if not user_repo.is_email_unique(new_user_data['email'], user_id):
            api.abort(409, 'L\'adresse e-mail existe déjà.')

        new_user_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        updated = user_repo.update_user(user_id, new_user_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Utilisateur non trouvé")
