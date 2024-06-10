#!/usr/bin/python3
"""Modèle pour la représentation des avis."""

class Review:
    """Classe représentant un avis."""
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = None
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        """Retourne les données de l'avis sous forme de dictionnaire."""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment
        }
