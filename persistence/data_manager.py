#!/usr/bin/python3
"""Gestionnaire de données pour les entités."""

from abc import ABC, abstractmethod
from model.user import User
from model.place import Place
from model.amenity import Amenity
from model.review import Review
from model.city import City
import uuid
from datetime import datetime

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

class UserRepository(DataManager):
    """Classe pour gérer la persistance et les opérations sur les utilisateurs."""
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, entity):
        """Sauvegarde un utilisateur."""
        if not hasattr(entity, 'user_id'):
            entity.user_id = str(uuid.uuid4())
            entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.users[entity.user_id] = entity

    def get(self, entity_id):
        """Récupère un utilisateur par son identifiant."""
        return self.users.get(entity_id)

    def get_all(self):
        """Récupère tous les utilisateurs."""
        return list(self.users.values())

    def update(self, entity_id, new_data):
        """Met à jour un utilisateur existant."""
        if entity_id in self.users:
            user = self.users[entity_id]
            user.update_user_data(new_data)
            self.save(user)
            return True
        return False

    def delete(self, entity_id):
        """Supprime un utilisateur existant."""
        if entity_id in self.users:
            del self.users[entity_id]
            return True
        return False

    def create_user(self, user_data):
        """Crée un nouveau utilisateur."""
        user = User(**user_data)
        self.save(user)
        return user.user_id

    def update_user(self, user_id, new_user_data):
        """Met à jour un utilisateur existant."""
        return self.update(user_id, new_user_data)

    def delete_user(self, user_id):
        """Supprime un utilisateur existant."""
        return self.delete(user_id)

    def get_all_users(self):
        """Récupère tous les utilisateurs."""
        return self.get_all()

    def get_user(self, user_id):
        """Récupère un utilisateur par son identifiant."""
        return self.get(user_id)

    def is_email_unique(self, email, user_id=None):
        """Vérifie si l'e-mail est unique."""
        for user in self.users.values():
            if user.email == email and user.user_id != user_id:
                return False
        return True

class PlaceRepository:
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

class AmenityRepository(DataManager):
    """Classe pour gérer la persistance des équipements."""
    def __init__(self):
        self.amenities = {}
        self.next_id = 1

    def save(self, entity):
        """Sauvegarde un équipement."""
        if not hasattr(entity, 'amenity_id'):
            entity.amenity_id = str(uuid.uuid4())
            entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.amenities[entity.amenity_id] = entity

    def get(self, entity_id):
        """Récupère un équipement par son identifiant."""
        return self.amenities.get(entity_id)

    def get_all(self):
        """Récupère tous les équipements."""
        return list(self.amenities.values())

    def update(self, entity_id, new_data):
        """Met à jour un équipement existant."""
        if entity_id in self.amenities:
            amenity = self.amenities[entity_id]
            amenity.update_amenity_data(new_data)
            self.save(amenity)
            return True
        return False

    def delete(self, entity_id):
        """Supprime un équipement existant."""
        if entity_id in self.amenities:
            del self.amenities[entity_id]
            return True
        return False

class ReviewRepository(DataManager):
    """Classe pour gérer la persistance des avis."""
    def __init__(self):
        self.reviews = {}
        self.next_id = 1

    def save(self, entity):
        """Sauvegarde un avis."""
        if not hasattr(entity, 'review_id'):
            entity.review_id = str(uuid.uuid4())
            entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.reviews[entity.review_id] = entity

    def get(self, entity_id):
        """Récupère un avis par son identifiant."""
        return self.reviews.get(entity_id)

    def get_all(self):
        """Récupère tous les avis."""
        return list(self.reviews.values())

    def update(self, entity_id, new_data):
        """Met à jour un avis existant."""
        if entity_id in self.reviews:
            review = self.reviews[entity_id]
            review.update_review_data(new_data)
            self.save(review)
            return True
        return False

    def delete(self, entity_id):
        """Supprime un avis existant."""
        if entity_id in self.reviews:
            del self.reviews[entity_id]
            return True
        return False

class CityRepository(DataManager):
    """Classe pour gérer la persistance des villes."""
    def __init__(self):
        self.cities = {}
        self.next_id = 1

    def save(self, entity):
        """Sauvegarde une ville."""
        if not hasattr(entity, 'city_id'):
            entity.city_id = str(uuid.uuid4())
            entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.cities[entity.city_id] = entity

    def get(self, entity_id):
        """Récupère une ville par son identifiant."""
        return self.cities.get(entity_id)

    def get_all(self):
        """Récupère toutes les villes."""
        return list(self.cities.values())

    def update(self, entity_id, new_data):
        """Met à jour une ville existante."""
        if entity_id in self.cities:
            city = self.cities[entity_id]
            city.update_city_data(new_data)
            self.save(city)
            return True
        return False

    def delete(self, entity_id):
        """Supprime une ville existante."""
        if entity_id in self.cities:
            del self.cities[entity_id]
            return True
        return False

    def is_name_unique(self, name, country_code):
        """Vérifie si le nom de la ville est unique dans un pays."""
        for city in self.cities.values():
            if city.name == name and city.country_code == country_code:
                return False
        return True
