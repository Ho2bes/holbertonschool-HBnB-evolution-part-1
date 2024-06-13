# test2/test_amenity.py

import unittest
import sys
import os
from model.amenity import Amenity

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        amenity = Amenity(name='WiFi')
        self.assertEqual(amenity.name, 'WiFi')
        self.assertIsNotNone(amenity.amenity_id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_to_dict(self):
        amenity = Amenity(name='WiFi')
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], 'WiFi')
        self.assertEqual(amenity_dict['amenity_id'], amenity.amenity_id)


if __name__ == '__main__':
    unittest.main()
