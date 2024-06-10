#!/usr/bin/python3
"""Gestionnaire de données pour les lieux."""

from abc import ABC, abstractmethod
from model_place import Place

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

class PlaceRepository(DataManager):
    """Classe pour gérer la persistance des lieux."""
    def __init__(self):
        self.places = {}
        self.next_id = 1

    def save(self, place):
        """Sauvegarde un lieu."""
        if not hasattr(place, 'place_id'):
            place.place_id = self.next_id
            self.next_id += 1
        self.places[place.place_id] = place

    def get(self, place_id):
        """Récupère un lieu."""
        return self.places.get(place_id)

    def get_all(self):
        """Récupère tous les lieux."""
        return list(self.places.values())

    def create_place(self, place_data):
        """Crée un nouveau lieu."""
        place = Place(**place_data)
        self.save(place)
        return place.place_id

    def update(self, place_id, new_place_data):
        """Met à jour un lieu existant."""
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_place_data)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        """Supprime un lieu existant."""
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False

class PlaceDataManager:
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
        place_id = len(self.repository.places) + 1
        place_data['place_id'] = place_id
        place = Place(**place_data)
        self.save(place)
        return place.place_id

    def update_place(self, place_id, new_place_data):
        """Met à jour un lieu existant."""
        return self.update(place_id, new_place_data)

    def delete_place(self, place_id):
        """Supprime un lieu existant."""
        return self.delete(place_id)
