#!/usr/bin/python3
"""Modèle pour la représentation des utilisateurs."""

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def update_user_data(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)
