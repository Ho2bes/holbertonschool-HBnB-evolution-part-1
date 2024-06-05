#!/usr/bin/python3
""" persistence code for place class"""
# persistence/place_repository.py

class PlaceRepository:
    """Classe pour simuler les opérations de persistance pour les lieux."""
    def __init__(self):
        self.places = {}

    def save_place(self, place_id, place_data):
        """Sauvegarde un lieu."""
        self.places[place_id] = place_data

    def get_place(self, place_id):
        """Récupère un lieu."""
        return self.places.get(place_id)

    # D'autres méthodes CRUD peuvent être ajoutées ici
