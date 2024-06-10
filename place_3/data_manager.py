#!/usr/bin/python3
"""Gestionnaire de données pour les lieux."""

from abc import ABC, abstractmethod

class DataManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, new_data):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

class PlaceDataManager(DataManager):
    """Classe pour gérer les opérations sur les lieux."""
    def __init__(self, repository):
        self.repository = repository

    def save(self, entity):
        """Sauvegarde un lieu."""
        self.repository.save(entity)

    def get(self, entity_id):
        """Récupère un lieu par son identifiant."""
        return self.repository.get(entity_id)

    def update(self, entity_id, new_data):
        """Met à jour un lieu existant."""
        return self.repository.update(entity_id, new_data)

    def delete(self, entity_id):
        """Supprime un lieu existant."""
        return self.repository.delete(entity_id)

    def get_all(self):
        """Récupère tous les lieux."""
        return self.repository.get_all()

    def get_all_places(self):
        """Récupère tous les lieux."""
        return self.get_all()

    def get_place(self, place_id):
        """Récupère un lieu par son identifiant."""
        return self.get(place_id)

    def create_place(self, place_data):
        """Crée un nouveau lieu."""
        place = Place(**place_data)
        self.save(place)
        return place.place_id

    def update_place(self, place_id, new_place_data):
        """Met à jour un lieu existant."""
        return self.update(place_id, new_place_data)

    def delete_place(self, place_id):
        """Supprime un lieu existant."""
        return self.delete(place_id)
