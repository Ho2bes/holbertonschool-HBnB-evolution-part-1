#!/usr/bin/python3
"""Définition du modèle User."""

from datetime import datetime
import uuid

class User:
    """Classe représentant un utilisateur."""

    def __init__(self, email, first_name, last_name):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_user_data(self, new_data):
        """Mise à jour des données utilisateur."""
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
