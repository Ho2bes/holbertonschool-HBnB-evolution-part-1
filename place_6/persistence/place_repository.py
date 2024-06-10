#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.place import Place

class PlaceRepository(IPersistenceManager):
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
