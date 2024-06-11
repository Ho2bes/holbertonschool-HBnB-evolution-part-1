#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask import request
from persistence.data_manager import DataManager

data_manager = DataManager()

api = Namespace('reviews', description='Opérations liées aux avis')

# Modèle de données pour la création d'un avis
review_model = api.model('Review', {
    'user_id': fields.Integer(required=True, description='ID de l\'utilisateur'),
    'place_id': fields.Integer(required=True, description='ID du lieu'),
    'rating': fields.Integer(required=True, description='Note'),
    'comment': fields.String(description='Commentaire')
})

@api.route('/')
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

@api.route('/<int:review_id>')
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
