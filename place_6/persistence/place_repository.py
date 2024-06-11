#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.place import Place

class PlaceRepository(IPersistenceManager):
    def __init__(self):
        self.places = {}
        self.next_id = 1

    def save(self, place):
        if not hasattr(place, 'place_id'):
            place.place_id = self.next_id
            self.next_id += 1
        self.places[place.place_id] = place

    def get(self, place_id):
        return self.places.get(place_id)

    def get_all(self):
        return list(self.places.values())

    def update(self, place_id, new_data):
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_data)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False

