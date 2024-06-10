#!/usr/bin/python3
"""Modèle pour la représentation des villes."""

from datetime import datetime
import uuid

class City:
    """Classe représentant une ville."""
    def __init__(self, name, country_code):
        self.city_id = str(uuid.uuid4())
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_city_data(self, new_data):
        """Mise à jour des données de la ville."""
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
