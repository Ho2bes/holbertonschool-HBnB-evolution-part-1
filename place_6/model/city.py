#!/usr/bin/python3
"""Modèle pour la représentation des villes."""

class City:
    """Classe représentant une ville."""
    def __init__(self, name, country_id):
        self.city_id = None
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        """Retourne les données de la ville sous forme de dictionnaire."""
        return {
            'city_id': self.city_id,
            'name': self.name,
            'country_id': self.country_id
        }
