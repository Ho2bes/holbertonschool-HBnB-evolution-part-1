#!/usr/bin/python3
"""Modèle pour la représentation des utilisateurs."""

class User:
    """Classe représentant un utilisateur."""
    def __init__(self, username, email, password):
        self.user_id = None
        self.username = username
        self.email = email
        self.password = password
        self.reviews = []

    def add_review(self, review):
        """Ajoute un commentaire."""
        self.reviews.append(review)

    def list_reviews(self):
        """Liste les commentaires."""
        return self.reviews

    def update_user_data(self, new_data):
        """Met à jour les données de l'utilisateur avec de nouvelles données."""
        for key, value in new_data.items():
            setattr(self, key, value)

    def check_password(self, password):
        """Vérifie si le mot de passe est correct."""
        return self.password == password

    def to_dict(self):
        """Retourne les données de l'utilisateur sous forme de dictionnaire."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'reviews': self.reviews
        }
