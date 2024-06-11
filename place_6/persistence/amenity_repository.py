#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.amenity import Amenity

class AmenityRepository(IPersistenceManager):
    def __init__(self):
        self.amenities = {}
        self.next_id = 1

    def save(self, amenity):
        if not hasattr(amenity, 'amenity_id'):
            amenity.amenity_id = self.next_id
            self.next_id += 1
        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
        return self.amenities.get(amenity_id)

    def get_all(self):
        return list(self.amenities.values())

    def update(self, amenity_id, new_data):
        if amenity_id in self.amenities:
            amenity = self.amenities[amenity_id]
            amenity.update_amenity_data(new_data)
            self.save(amenity)
            return True
        return False

    def delete(self, amenity_id):
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False

