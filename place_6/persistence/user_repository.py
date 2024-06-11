#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.user import User

class UserRepository(IPersistenceManager):
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, user):
        if not hasattr(user, 'user_id'):
            user.user_id = self.next_id
            self.next_id += 1
        self.users[user.user_id] = user

    def get(self, user_id):
        return self.users.get(user_id)

    def get_all(self):
        return list(self.users.values())

    def update(self, user_id, new_data):
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_data)
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
