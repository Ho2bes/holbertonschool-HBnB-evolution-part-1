import unittest
from country import Country  # Assurez-vous que le nom du fichier contenant la classe Country est "country.py"

class TestCountry(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.name = "France"
        self.country = Country(self.name)

    def test_country_creation(self):
        """Test if the country is created with correct attributes."""
        self.assertEqual(self.country.name, self.name)
        self.assertIsNone(self.country.country_id)

    def test_to_dict(self):
        """Test the to_dict method."""
        country_dict = self.country.to_dict()
        self.assertEqual(country_dict['country_id'], self.country.country_id)
        self.assertEqual(country_dict['name'], self.country.name)

if __name__ == '__main__':
    unittest.main()
