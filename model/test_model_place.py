#!/usr/bin/python3

import unittest
from model_place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place("Paris", 4, 2)

    def test_add_review(self):
        self.place.add_review("Great place to stay!")
        self.assertEqual(len(self.place.reviews), 1)
        self.assertEqual(self.place.reviews[0], "Great place to stay!")

    def test_calculate_total_price(self):
        nightly_rate = 100
        total_price = self.place.calculate_total_price(nightly_rate)
        self.assertEqual(total_price, 400)  # 100 * 4 guests

    def test_list_amenities(self):
        self.assertEqual(self.place.list_amenities(), [])

    def test_check_availability(self):
        self.assertTrue(self.place.check_availability())

    def test_set_number_guests(self):
        self.place.set_number_guests(6)
        self.assertEqual(self.place.number_guests, 6)

    # Ajoutez d'autres méthodes de test selon vos besoins

if __name__ == '__main__':
    unittest.main()
