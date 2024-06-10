#!/usr/bin/python3

import unittest
from model_place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Test Place",
            description="A nice place",
            address="123 Street",
            city_id=1,
            latitude=45.0,
            longitude=-75.0,
            host_id=1,
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=["1", "2"]
        )

    def test_add_review(self):
        self.place.add_review("Great place!")
        self.assertIn("Great place!", self.place.reviews)

    def test_calculate_total_price(self):
        total_price = self.place.calculate_total_price()
        self.assertEqual(total_price, 400.0)

    def test_list_amenities(self):
        amenities = self.place.list_amenities()
        self.assertEqual(amenities, ["1", "2"])

    def test_set_number_of_guests(self):
        self.place.set_number_of_guests(5)
        self.assertEqual(self.place.max_guests, 5)

    def test_add_description(self):
        self.place.add_description("Updated description")
        self.assertEqual(self.place.description, "Updated description")

    def test_set_number_of_rooms(self):
        self.place.set_number_of_rooms(4)
        self.assertEqual(self.place.number_of_rooms, 4)

    def test_set_location(self):
        self.place.set_location(46.0, -76.0)
        self.assertEqual(self.place.latitude, 46.0)
        self.assertEqual(self.place.longitude, -76.0)

    def test_add_amenity(self):
        self.place.add_amenity("3")
        self.assertIn("3", self.place.amenity_ids)

    def test_get_description(self):
        description = self.place.get_description()
        self.assertEqual(description, "A nice place")

    def test_get_location(self):
        location = self.place.get_location()
        self.assertEqual(location, (45.0, -75.0))

    def test_update_place_data(self):
        new_data = {"name": "Updated Place", "description": "Updated description"}
        self.place.update_place_data(new_data)
        self.assertEqual(self.place.name, "Updated Place")
        self.assertEqual(self.place.description, "Updated description")

    def test_delete_amenity(self):
        self.place.delete_amenity("1")
        self.assertNotIn("1", self.place.amenity_ids)

if __name__ == '__main__':
    unittest.main()
