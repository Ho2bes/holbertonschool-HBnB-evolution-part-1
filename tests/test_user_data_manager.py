import unittest
from persistence.data_manager import UserDataManager
from model import user

class TestUserDataManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserDataManager()

    def test_create_user(self):
        user_data = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        user_id = self.manager.create_user(user_data)
        user = self.manager.get_user(user_id)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_update_user(self):
        user_data = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        user_id = self.manager.create_user(user_data)
        new_data = {'first_name': 'Jane'}
        self.manager.update_user(user_id, new_data)
        user = self.manager.get_user(user_id)
        self.assertEqual(user.first_name, 'Jane')

    def test_delete_user(self):
        user_data = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        user_id = self.manager.create_user(user_data)
        self.manager.delete_user(user_id)
        user = self.manager.get_user(user_id)
        self.assertIsNone(user)

    def test_get_all_users(self):
        user_data1 = {'email': 'test1@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        user_data2 = {'email': 'test2@example.com', 'first_name': 'Jane', 'last_name': 'Doe'}
        self.manager.create_user(user_data1)
        self.manager.create_user(user_data2)
        users = self.manager.get_all_users()
        self.assertEqual(len(users), 2)

if __name__ == '__main__':
    unittest.main()
