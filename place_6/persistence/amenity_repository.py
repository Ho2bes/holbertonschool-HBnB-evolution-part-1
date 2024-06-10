#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.amenity import Amenity

class AmenityRepository(IPersistenceManager):
    """Classe pour gérer la persistance des équipements."""
    def __init__(self):
        self.amenities = {}
        self.next_id = 1

    def save(self, amenity):
        """Sauvegarde un équipement."""
        if not hasattr(amenity, 'amenity_id'):
            amenity.amenity_id = self.next_id
            self.next_id += 1
        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
        """Récupère un équipement."""
        return self.amenities.get(amenity_id)

    def get_all(self):
        """Récupère tous les équipements."""
        return list(self.amenities.values())

    def update(self, amenity_id, new_amenity_data):
        """Met à jour un équipement existant."""
        if amenity_id in self.amenities:
            amenity = self.amenities[amenity_id]
            for key, value in new_amenity_data.items():
                setattr(amenity, key, value)
            self.save(amenity)
            return True
        return False

    def delete(self, amenity_id):
        """Supprime un équipement existant."""
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False
