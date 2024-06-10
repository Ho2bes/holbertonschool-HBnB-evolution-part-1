import unittest
import json
from api_place import app, place_data_manager

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_places(self):
        response = self.app.get('/places')
        self.assertEqual(response.status_code, 200)

    def test_post_place(self):
        new_place = {
            "name": "Test Place",
            "description": "A place for testing",
            "address": "123 Test St",
            "city_id": 1,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": 1,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": ["wifi", "pool"]
        }
        response = self.app.post('/places', data=json.dumps(new_place), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Lieu créé avec succès', json.loads(response.data.decode())['message'])

    def test_get_place(self):
        place_id = 1
        response = self.app.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 404)  # Assumes place_id 1 does not exist initially

    def test_delete_place(self):
        place_id = 1
        response = self.app.delete(f'/places/{place_id}')
        self.assertEqual(response.status_code, 404)  # Assumes place_id 1 does not exist initially

    def test_put_place(self):
        # Create a place first to ensure there is something to update
        new_place = {
            "name": "Test Place",
            "description": "A place for testing",
            "address": "123 Test St",
            "city_id": 1,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": 1,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": ["wifi", "pool"]
        }
        post_response = self.app.post('/places', data=json.dumps(new_place), content_type='application/json')
        place_id = json.loads(post_response.data.decode())['place_id']

        updated_place = {
            "name": "Updated Place",
            "description": "An updated place for testing",
            "address": "123 Updated St",
            "city_id": 1,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": 1,
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["wifi", "pool", "gym"]
        }
        response = self.app.put(f'/places/{place_id}', data=json.dumps(updated_place), content_type='application/json')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
