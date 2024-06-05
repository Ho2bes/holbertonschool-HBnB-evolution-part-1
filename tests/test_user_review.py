#!/usr/bin/python3

import unittest
from User_review import Review

class test_user_review(unittest.TestCase):
      def setUp(self):
        # Initialisation pour chaque test
        self.review = Review()

        def test_add_review(self):
              # Test d'ajout d'un avis
              self.review.add_review("Great product")
              self.assertEqual(self.review.reviews, ["Great product"])

              def test_modify_review(self):
                    # Test de modification d'un avis
                    self.review.add_review("Great product")
                    self.review.modify_review(0, "Awesome product")
                    self.assertEqual(self.review.reviews, ["Awesome product"])

                    def test_delete_review(self):
                         # Test de suppression d'un avis
                         self.review.add_review("Great product")
                         self.review.delete_review(0)
                         self.assertEqual(self.review.reviews, [])

                         def test_display_reviews(self):
                              # Test d'affichage des avis
                              self.review.add_review("Great product")
                              self.review.add_review("Terrible service")
                              self.review.add_review("Average experience")
                              captured_output = io.StringIO()
                              sys.stdout = captured_output
                              self.review.display_reviews()
                              sys.stdout = sys.__stdout__
                              self.assertEqual(captured_output.getvalue(), "Great product\nTerrible service\nAverage experience\n")

if __name__ == '__main__':
    unittest.main()
