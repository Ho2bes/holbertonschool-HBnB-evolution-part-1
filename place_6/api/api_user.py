#!/usr/bin/python3


from flask_restx import Namespace, Resource, fields
from flask import request
from persistence.data_manager import DataManager

data_manager = DataManager()

api = Namespace('users', description='Opérations liées aux utilisateurs')

# Modèle de données pour la création d'un utilisateur
user_model = api.model('User', {
    'username': fields.String(required=True, description='Nom d\'utilisateur'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Mot de passe')
})

@api.route('/')
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

@api.route('/<int:user_id>')
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

