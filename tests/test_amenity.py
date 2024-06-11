import unittest
from model.amenity import Amenity
from persistence.data_manager import AmenityRepository

class TestAmenityModel(unittest.TestCase):

    def setUp(self):
        self.amenity_repo = AmenityRepository()
        self.amenity_data = {
            'name': 'WiFi'
        }

    def test_create_amenity(self):
        amenity = Amenity(self.amenity_data['name'])
        self.amenity_repo.save(amenity)
        saved_amenity = self.amenity_repo.get(amenity.amenity_id)
        self.assertEqual(saved_amenity.name, self.amenity_data['name'])

    def test_update_amenity(self):
        amenity = Amenity(self.amenity_data['name'])
        self.amenity_repo.save(amenity)
        new_data = {'name': 'Updated WiFi'}
        self.amenity_repo.update(amenity.amenity_id, new_data)
        updated_amenity = self.amenity_repo.get(amenity.amenity_id)
        self.assertEqual(updated_amenity.name, 'Updated WiFi')

    def test_delete_amenity(self):
        amenity = Amenity(self.amenity_data['name'])
        self.amenity_repo.save(amenity)
        self.amenity_repo.delete(amenity.amenity_id)
        deleted_amenity = self.amenity_repo.get(amenity.amenity_id)
        self.assertIsNone(deleted_amenity)

if __name__ == '__main__':
    unittest.main()
