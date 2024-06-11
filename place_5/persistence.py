#!/usr/bin/python3


from abc import ABC, abstractmethod
from model_place import Place
from model_user import User
from model_review import Review
from model_amenity import Amenity
from model_country import Country
from model_city import City

class IPersistenceManager(ABC):
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

class UserRepository(IPersistenceManager):
    """Classe pour gérer la persistance des utilisateurs."""
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, user):
        """Sauvegarde un utilisateur."""
        if not hasattr(user, 'user_id'):
            user.user_id = self.next_id
            self.next_id += 1
        self.users[user.user_id] = user

    def get(self, user_id):
        """Récupère un utilisateur."""
        return self.users.get(user_id)

    def get_all(self):
        """Récupère tous les utilisateurs."""
        return list(self.users.values())

    def update(self, user_id, new_user_data):
        """Met à jour un utilisateur existant."""
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_user_data)
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        """Supprime un utilisateur existant."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

class ReviewRepository(IPersistenceManager):
    """Classe pour gérer la persistance des avis."""
    def __init__(self):
        self.reviews = {}
        self.next_id = 1

    def save(self, review):
        """Sauvegarde un avis."""
        if not hasattr(review, 'review_id'):
            review.review_id = self.next_id
            self.next_id += 1
        self.reviews[review.review_id] = review

    def get(self, review_id):
        """Récupère un avis."""
        return self.reviews.get(review_id)

    def get_all(self):
        """Récupère tous les avis."""
        return list(self.reviews.values())

    def update(self, review_id, new_review_data):
        """Met à jour un avis existant."""
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                setattr(review, key, value)
            self.save(review)
            return True
        return False

    def delete(self, review_id):
        """Supprime un avis existant."""
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False

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
