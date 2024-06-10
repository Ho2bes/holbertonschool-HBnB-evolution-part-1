#!/usr/bin/python3
"""Modèle pour la représentation des équipements (amenities)."""

from datetime import datetime
import uuid

class Amenity:
    """Classe représentant un équipement."""
    def __init__(self, name):
        self.amenity_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_amenity_data(self, new_data):
        """Mise à jour des données de l'équipement."""
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
