#!/usr/bin/python3
"""Modèle pour la représentation des pays."""

class Country:
    """Classe représentant un pays."""
    def __init__(self, name):
        self.country_id = None
        self.name = name

    def to_dict(self):
        """Retourne les données du pays sous forme de dictionnaire."""
        return {
            'country_id': self.country_id,
            'name': self.name
        }
