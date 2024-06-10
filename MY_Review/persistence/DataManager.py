#!/usr/bin/python3

class DataManager(IPersistence_Manager):
    def __init__(self):
        self.storage = {}  # Dictionnaire pour simuler le stockage en mémoire

    def save(self, entity):
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
        entity_id = entity.review_id
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
