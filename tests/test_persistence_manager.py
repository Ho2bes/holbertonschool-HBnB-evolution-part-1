import unittest
import sys
import os
from datetime import datetime
from persistence.ipersistence_manager import IPersistenceManager

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestEntity:
    """A simple entity class for testing."""
    def __init__(self, entity_id, name):
        self.entity_id = entity_id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()


class ConcretePersistenceManager(IPersistenceManager):
    """A concrete implementation of IPersistenceManager for testing."""
    def __init__(self):
        self.entities = {}

    def save(self, entity):
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.entities[entity.entity_id] = entity

    def get(self, entity_id):
        return self.entities.get(entity_id)

    def update(self, entity_id, new_data):
        if entity_id in self.entities:
            entity = self.entities[entity_id]
            entity.update(new_data)
            self.save(entity)
            return True
        return False

    def delete(self, entity_id):
        if entity_id in self.entities:
            del self.entities[entity_id]
            return True
        return False

    def get_all(self):
        return list(self.entities.values())


class TestIPersistenceManager(unittest.TestCase):

    def setUp(self):
        self.persistence_manager = ConcretePersistenceManager()

    def test_save_entity(self):
        entity = TestEntity(entity_id='1', name='Test Entity')
        self.persistence_manager.save(entity)
        self.assertIn(entity.entity_id, self.persistence_manager.entities)

    def test_get_entity(self):
        entity = TestEntity(entity_id='1', name='Test Entity')
        self.persistence_manager.save(entity)
        fetched = self.persistence_manager.get(entity.entity_id)
        self.assertEqual(fetched.name, 'Test Entity')

    def test_update_entity(self):
        entity = TestEntity(entity_id='1', name='Test Entity')
        self.persistence_manager.save(entity)
        update_data = {'name': 'Updated Entity'}
        self.persistence_manager.update(entity.entity_id, update_data)
        updated = self.persistence_manager.get(entity.entity_id)
        self.assertEqual(updated.name, 'Updated Entity')

    def test_delete_entity(self):
        entity = TestEntity(entity_id='1', name='Test Entity')
        self.persistence_manager.save(entity)
        self.persistence_manager.delete(entity.entity_id)
        self.assertIsNone(self.persistence_manager.get(entity.entity_id))

    def test_get_all_entities(self):
        entity1 = TestEntity(entity_id='1', name='Entity 1')
        entity2 = TestEntity(entity_id='2', name='Entity 2')
        self.persistence_manager.save(entity1)
        self.persistence_manager.save(entity2)
        all_entities = self.persistence_manager.get_all()
        self.assertEqual(len(all_entities), 2)


if __name__ == '__main__':
    unittest.main()
