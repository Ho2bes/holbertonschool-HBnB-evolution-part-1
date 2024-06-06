#!/usr/bin/python3

import unittest
from unittest.mock import MagicMock
from MY_Review.persistence.persistence_manager import PersistenceManager
from MY_Review.model.review import Review

class TestPersistenceManager(unittest.TestCase):
    def setUp(self):
        # Création d'un gestionnaire de persistance avec un mock de la couche de stockage
        self.storage_mock = MagicMock()
        self.persistence_manager = PersistenceManager(self.storage_mock)

    def test_save_review(self):
        # Création d'une revue
        review = Review(1, "Great product", 5)

        # Appel de la méthode de sauvegarde du gestionnaire de persistance
        self.persistence_manager.save(review)

        # Vérification que la méthode de sauvegarde du stockage a été appelée avec la revue en argument
        self.storage_mock.save.assert_called_once_with(review)

    def test_delete_review(self):
        # Appel de la méthode de suppression du gestionnaire de persistance avec l'identifiant de la revue
        self.persistence_manager.delete(1)

        # Vérification que la méthode de suppression du stockage a été appelée avec l'identifiant de la revue en argument
        self.storage_mock.delete.assert_called_once_with(1)

    # Ajoutez d'autres méthodes de test pour les opérations de lecture et de mise à jour si nécessaire

if __name__ == '__main__':
    unittest.main()
