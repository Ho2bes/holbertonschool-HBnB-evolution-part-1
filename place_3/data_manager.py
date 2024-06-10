#!/usr/bin/python3
"""Gestionnaire de données pour les lieux."""


class PlaceDataManager:
    """Classe pour gérer les opérations sur les lieux."""
    def __init__(self, repository):
        self.repository = repository

    def get_all_places(self):
        """Récupère tous les lieux."""
        return self.repository.get_all_places()

    def get_place(self, place_id):
        """Récupère un lieu par son identifiant."""
        return self.repository.get_place(place_id)

    def create_place(self, place_data):
        """Crée un nouveau lieu."""
        return self.repository.create_place(place_data)

    def update_place(self, place_id, new_place_data):
        """Met à jour un lieu existant."""
        return self.repository.update_place(place_id, new_place_data)

    def delete_place(self, place_id):
        """Supprime un lieu existant."""
        return self.repository.delete_place(place_id)
