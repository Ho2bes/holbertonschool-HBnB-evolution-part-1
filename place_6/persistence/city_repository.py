#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.city import City

class CityRepository(IPersistenceManager):
    """Classe pour gérer la persistance des villes."""
    def __init__(self):
        self.cities = {}
        self.next_id = 1

    def save(self, city):
        """Sauvegarde une ville."""
        if not hasattr(city, 'city_id'):
            city.city_id = self.next_id
            self.next_id += 1
        self.cities[city.city_id] = city

    def get(self, city_id):
        """Récupère une ville."""
        return self.cities.get(city_id)

    def get_all(self):
        """Récupère toutes les villes."""
        return list(self.cities.values())

    def update(self, city_id, new_city_data):
        """Met à jour une ville existante."""
        if city_id in self.cities:
            city = self.cities[city_id]
            for key, value in new_city_data.items():
                setattr(city, key, value)
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        """Supprime une ville existante."""
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False
