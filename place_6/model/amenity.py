#!/usr/bin/python3
"""Modèle pour la représentation des équipements."""

class Amenity:
    """Classe représentant un équipement."""
    def __init__(self, name):
        self.amenity_id = None
        self.name = name

    def to_dict(self):
        """Retourne les données de l'équipement sous forme de dictionnaire."""
        return {
            'amenity_id': self.amenity_id,
            'name': self.name
        }
