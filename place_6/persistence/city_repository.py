#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.city import City

class CityRepository(IPersistenceManager):
    def __init__(self):
        self.cities = {}
        self.next_id = 1

    def save(self, city):
        if not hasattr(city, 'city_id'):
            city.city_id = self.next_id
            self.next_id += 1
        self.cities[city.city_id] = city

    def get(self, city_id):
        return self.cities.get(city_id)

    def get_all(self):
        return list(self.cities.values())

    def update(self, city_id, new_data):
        if city_id in self.cities:
            city = self.cities[city_id]
            city.update_city_data(new_data)
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False
