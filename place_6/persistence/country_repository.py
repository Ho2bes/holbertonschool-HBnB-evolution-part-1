#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.country import Country

class CountryRepository(IPersistenceManager):
    """Classe pour gérer la persistance des pays."""
    def __init__(self):
        self.countries = {}
        self.next_id = 1

    def save(self, country):
        """Sauvegarde un pays."""
        if not hasattr(country, 'country_id'):
            country.country_id = self.next_id
            self.next_id += 1
        self.countries[country.country_id] = country

    def get(self, country_id):
        """Récupère un pays."""
        return self.countries.get(country_id)

    def get_all(self):
        """Récupère tous les pays."""
        return list(self.countries.values())

    def update(self, country_id, new_country_data):
        """Met à jour un pays existant."""
        if country_id in self.countries:
            country = self.countries[country_id]
            for key, value in new_country_data.items():
                setattr(country, key, value)
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        """Supprime un pays existant."""
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False
