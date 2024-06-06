#!/usr/bin/python3
"""Code de persistance pour la classe Place."""

class PlaceRepository:
    """Classe pour gérer la persistance des lieux."""
    def __init__(self):
        self.places = {}

    def save_place(self, place_id, place_data):
        """Sauvegarde un lieu."""
        self.places[place_id] = place_data

    def get_place(self, place_id):
        """Récupère un lieu."""
        return self.places.get(place_id)

    # D'autres méthodes CRUD peuvent être ajoutées ici
