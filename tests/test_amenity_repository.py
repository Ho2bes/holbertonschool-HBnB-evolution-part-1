import unittest
import sys
import os
from model.amenity import Amenity
from persistence.amenity_repository import AmenityRepository

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAmenityRepository(unittest.TestCase):

    def setUp(self):
        self.repo = AmenityRepository()

    def test_save_amenity(self):
        amenity = Amenity(name='WiFi')
        self.repo.save(amenity)
        self.assertIn(amenity.amenity_id, self.repo.amenities)

    def test_get_amenity(self):
        amenity = Amenity(name='WiFi')
        self.repo.save(amenity)
        fetched = self.repo.get(amenity.amenity_id)
        self.assertEqual(fetched.name, 'WiFi')

    def test_update_amenity(self):
        amenity = Amenity(name='WiFi')
        self.repo.save(amenity)
        update_data = {'name': 'Updated WiFi'}
        self.repo.update(amenity.amenity_id, update_data)
        updated = self.repo.get(amenity.amenity_id)
        self.assertEqual(updated.name, 'Updated WiFi')

    def test_delete_amenity(self):
        amenity = Amenity(name='WiFi')
        self.repo.save(amenity)
        self.repo.delete(amenity.amenity_id)
        self.assertIsNone(self.repo.get(amenity.amenity_id))


if __name__ == '__main__':
    unittest.main()
