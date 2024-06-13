import unittest
import sys
import os
from model.user import User

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        self.assertEqual(user.username, 'testuser')
        self.assertIsNotNone(user.user_id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_to_dict(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['username'], 'testuser')
        self.assertEqual(user_dict['user_id'], user.user_id)


if __name__ == '__main__':
    unittest.main()
