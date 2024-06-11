#!/usr/bin/python3

from flask import Flask, jsonify, request
from abc import ABC, abstractmethod

# Interface IPersistenceManager
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

# Implémentation de DataManager
class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}  # Dictionnaire pour simuler le stockage en mémoire

    def save(self, entity):
        if not hasattr(entity, 'review_id'):
            raise AttributeError("L'entité doit avoir un attribut 'review_id'")
        entity_id = entity.review_id
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

# Définition de la classe Review
class Review:
    def __init__(self, review_id, feedback, rating):
        self.review_id = review_id
        self.feedback = feedback
        self.rating = rating

    def edit_feedback(self, new_feedback):
        self.feedback = new_feedback

    def edit_rating(self, new_rating):
        self.rating = new_rating

app = Flask(__name__)
data_manager = DataManager()

@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review_id = len(data_manager.storage.get('Review', {})) + 1
    feedback = data.get('feedback')
    rating = data.get('rating')

    review = Review(review_id, feedback, rating)
    data_manager.save(review)

    return jsonify({'message': 'Review created successfully'}), 201

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews = data_manager.storage.get('Review', {}).values()
    return jsonify({'reviews': [review.__dict__ for review in reviews]})

if __name__ == '__main__':
    app.run(debug=True)
