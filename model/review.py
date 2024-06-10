#!/usr/bin/python3
"""Modèle pour la représentation des avis (reviews)."""

from datetime import datetime
import uuid

class Review:
    """Classe représentant un avis."""
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_review_data(self, new_data):
        """Mise à jour des données de l'avis."""
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
