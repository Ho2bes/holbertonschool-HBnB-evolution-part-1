import unittest
from model.user import User
from persistence.data_manager import UserRepository

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.user_repo = UserRepository()
        self.user_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password123'
        }

    def test_create_user(self):
        user_id = self.user_repo.create_user(self.user_data)
        user = self.user_repo.get(user_id)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])

    def test_unique_email(self):
        self.user_repo.create_user(self.user_data)
        with self.assertRaises(ValueError) as context:
            self.user_repo.create_user(self.user_data)  # Should raise an exception for duplicate email
        self.assertTrue('Email address already exists.' in str(context.exception))

    def test_update_user(self):
        user_id = self.user_repo.create_user(self.user_data)
        new_data = {'first_name': 'Updated'}
        self.user_repo.update_user(user_id, new_data)
        user = self.user_repo.get(user_id)
        self.assertEqual(user.first_name, 'Updated')

    def test_delete_user(self):
        user_id = self.user_repo.create_user(self.user_data)
        self.user_repo.delete_user(user_id)
        user = self.user_repo.get(user_id)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
