# test2/test_user_repository.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.user import User
from persistence.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repo = UserRepository()

    def test_save_user(self):
        user = User(username='testuser', email='testuser@example.com', password='password')
        self.repo.save(user)
        self.assertIn(user.user_id, self.repo.users)

    def test_get_user(self):
        user = User(username='testuser', email='testuser@example.com', password='password')
        self.repo.save(user)
        fetched = self.repo.get(user.user_id)
        self.assertEqual(fetched.username, 'testuser')

    def test_update_user(self):
        user = User(username='testuser', email='testuser@example.com', password='password')
        self.repo.save(user)
        update_data = {'username': 'updateduser'}
        self.repo.update(user.user_id, update_data)
        updated = self.repo.get(user.user_id)
        self.assertEqual(updated.username, 'updateduser')

    def test_delete_user(self):
        user = User(username='testuser', email='testuser@example.com', password='password')
        self.repo.save(user)
        self.repo.delete(user.user_id)
        self.assertIsNone(self.repo.get(user.user_id))

if __name__ == '__main__':
    unittest.main()
