#!/usr/bin/python3

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}  # Dictionnaire pour simuler le stockage en mémoire

    def save(self, entity):
        if not hasattr(entity, 'review_id'):
            raise AttributeError("L'entité doit avoir un attribut 'review_id'")
        entity_id = entity.review_id  # Suppose que toutes les entités ont un attribut review_id
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        return None

    def update(self, entity):
        if not hasattr(entity, 'review_id'):
            raise AttributeError("L'entité doit avoir un attribut 'review_id'")
        entity_id = entity.review_id
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]

# Exemple d'utilisation et test
class Review:
    def __init__(self, review_id, feedback, rating):
        self.review_id = review_id
        self.feedback = feedback
        self.rating = rating

    def edit_feedback(self, new_feedback):
        self.feedback = new_feedback

    def edit_rating(self, new_rating):
        self.rating = new_rating

# Créer un DataManager et une Review pour tester
data_manager = DataManager()
review = Review(1, "Great product!", 5)
data_manager.save(review)
retrieved_review = data_manager.get(1, 'Review')
print(retrieved_review.feedback)  # Devrait afficher "Great product!"
