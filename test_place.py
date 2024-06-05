import unittest

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user1 = User("Alice", "alice@example.com")
        self.place1 = Place("Paris", 4, 2)

    def test_created_at_and_updated_at(self):
        # Vérifier que les champs created_at et updated_at sont automatiquement définis lors de la création et de la mise à jour
        self.assertIsNotNone(self.place1.created_at)
        self.assertIsNotNone(self.place1.updated_at)

    def test_relationships(self):
        # Vérifier l'intégrité des relations
        self.place1.add_host(self.user1)
        self.assertEqual(self.place1.host, self.user1)

    def test_business_rules(self):
        # Vérifier l'application des règles métier
        with self.assertRaises(Exception):
            self.place1.add_host(User("Bob", "bob@example.com"))  # Tentative d'ajouter un deuxième hôte

    def test_place_instantiation(self):
        # Vérifier l'instanciation d'un lieu avec tous les champs requis
        self.assertEqual(self.place1.location, "Paris")
        self.assertEqual(self.place1.number_guests, 4)
        self.assertEqual(self.place1.number_rooms, 2)

    def test_host_assignment(self):
        # Vérifier les règles d'attribution d'hôte
        self.place1.add_host(self.user1)
        self.assertEqual(self.place1.host, self.user1)

    def test_amenity_addition(self):
        # Vérifier l'ajout d'équipements à un lieu
        self.place1.add_amenity("WiFi")
        self.assertIn("WiFi", self.place1.amenities)

    def test_retrieve_and_update_amenities(self):
        # Vérifier la récupération et la mise à jour des équipements
        self.place1.add_amenity("WiFi")
        amenities = self.place1.list_amenities()
        self.assertIn("WiFi", amenities)
        self.place1.amenities.remove("WiFi")
        self.assertNotIn("WiFi", self.place1.amenities)

if __name__ == '__main__':
    unittest.main()
