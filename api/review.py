#!/usr/bin/python3
"""API pour la gestion des avis (reviews)."""

from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace
from model.review import Review
from persistence.data_manager import ReviewRepository

api = Namespace('reviews', description='API pour la gestion des avis')

# Initialisation du référentiel d'avis
review_repo = ReviewRepository()

# Modèle de données pour la création d'un avis
review_model = api.model('Review', {
    'user_id': fields.String(required=True, description='ID de l\'utilisateur'),
    'place_id': fields.String(required=True, description='ID du lieu'),
    'rating': fields.Integer(required=True, description='Note', min=1, max=5),
    'comment': fields.String(required=True, description='Commentaire')
})

@api.route('/')
class Reviews(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Récupère tous les avis."""
        all_reviews = review_repo.get_all()
        return all_reviews

    @api.expect(review_model)
    @api.response(201, 'Avis créé avec succès')
    @api.response(400, 'Requête invalide')
    def post(self):
        """Crée un nouvel avis."""
        new_review_data = request.json
        if not all(key in new_review_data for key in ('user_id', 'place_id', 'rating', 'comment')):
            api.abort(400, 'Les champs user_id, place_id, rating et comment sont requis.')
        review_id = review_repo.create(new_review_data)
        response_message = {'message': 'Avis créé avec succès', 'review_id': review_id}
        return response_message, 201

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    @api.response(404, 'Avis non trouvé')
    def get(self, review_id):
        """Récupère un avis par son identifiant."""
        review_data = review_repo.get(review_id)
        if review_data:
            return review_data
        else:
            api.abort(404, "Avis non trouvé")

    @api.response(204, 'Avis supprimé avec succès')
    @api.response(404, 'Avis non trouvé')
    def delete(self, review_id):
        """Supprime un avis existant."""
        deleted = review_repo.delete(review_id)
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
        if not all(key in new_review_data for key in ('user_id', 'place_id', 'rating', 'comment')):
            api.abort(400, 'Les champs user_id, place_id, rating et comment sont requis.')
        updated = review_repo.update(review_id, new_review_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Avis non trouvé")
