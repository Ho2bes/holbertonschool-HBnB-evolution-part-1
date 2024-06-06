#!/usr/bin/python3

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def retrieve(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass
