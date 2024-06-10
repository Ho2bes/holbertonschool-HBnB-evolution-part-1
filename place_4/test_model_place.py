
import unittest
from model_place import Place

class PlaceModelTestCase(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Test Place",
            description="A place for testing",
            address="123 Test St",
            city_id=1,
            latitude=40.7128,
            longitude=-74.0060,
            host_id=1,
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=["wifi", "pool"]
        )

    def test_initialization(self):
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "A place for testing")
        self.assertEqual(self.place.address, "123 Test St")
        self.assertEqual(self.place.city_id, 1)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.host_id, 1)
        self.assertEqual(self.place.number_of_rooms, 2)
        self.assertEqual(self.place.number_of_bathrooms, 1)
        self.assertEqual(self.place.price_per_night, 100.0)
        self.assertEqual(self.place.max_guests, 4)
        self.assertEqual(self.place.amenity_ids, ["wifi", "pool"])

    def test_add_review(self):
        review = "Great place!"
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)

    def test_calculate_total_price(self):
        self.assertEqual(self.place.calculate_total_price(), 400.0)

    def test_list_amenities(self):
        self.assertEqual(self.place.list_amenities(), ["wifi", "pool"])

    def test_update_place_data(self):
        new_data = {
            "name": "Updated Place",
            "description": "An updated place for testing",
            "address": "456 Updated St",
            "city_id": 2,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "host_id": 2,
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["wifi", "pool", "gym"]
        }
        self.place.update_place_data(new_data)
        self.assertEqual(self.place.name, "Updated Place")
        self.assertEqual(self.place.description, "An updated place for testing")
        self.assertEqual(self.place.address, "456 Updated St")
        self.assertEqual(self.place.city_id, 2)
        self.assertEqual(self.place.latitude, 34.0522)
        self.assertEqual(self.place.longitude, -118.2437)
        self.assertEqual(self.place.host_id, 2)
        self.assertEqual(self.place.number_of_rooms, 3)
        self.assertEqual(self.place.number_of_bathrooms, 2)
        self.assertEqual(self.place.price_per_night, 150.0)
        self.assertEqual(self.place.max_guests, 5)
        self.assertEqual(self.place.amenity_ids, ["wifi", "pool", "gym"])

    def test_delete_amenity(self):
        self.place.delete_amenity("wifi")
        self.assertNotIn("wifi", self.place.amenity_ids)

    def test_set_number_of_guests(self):
        self.place.set_number_of_guests(6)
        self.assertEqual(self.place.max_guests, 6)

    def test_add_description(self):
        self.place.add_description("Updated description")
        self.assertEqual(self.place.description, "Updated description")

    def test_set_number_of_rooms(self):
        self.place.set_number_of_rooms(4)
        self.assertEqual(self.place.number_of_rooms, 4)

    def test_set_location(self):
        self.place.set_location(37.7749, -122.4194)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)

    def test_add_amenity(self):
        self.place.add_amenity("gym")
        self.assertIn("gym", self.place.amenity_ids)

    def test_get_description(self):
        self.assertEqual(self.place.get_description(), "A place for testing")

    def test_get_location(self):
        self.assertEqual(self.place.get_location(), (40.7128, -74.0060))

    def test_list_reviews(self):
        review1 = "Great place!"
        review2 = "Would stay again!"
        self.place.add_review(review1)
        self.place.add_review(review2)
        self.assertEqual(self.place.list_reviews(), [review1, review2])

if __name__ == '__main__':
    unittest.main()
