#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.country import Country

class CountryRepository(IPersistenceManager):
    def __init__(self):
        self.countries = {}
        self.next_id = 1

    def save(self, country):
        if not hasattr(country, 'country_id'):
            country.country_id = self.next_id
            self.next_id += 1
        self.countries[country.country_id] = country

    def get(self, country_id):
        return self.countries.get(country_id)

    def get_all(self):
        return list(self.countries.values())

    def update(self, country_id, new_data):
        if country_id in self.countries:
            country = self.countries[country_id]
            country.update_country_data(new_data)
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False
