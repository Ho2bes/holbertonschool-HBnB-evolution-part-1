#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.user import User

class UserRepository(IPersistenceManager):
    """Classe pour gérer la persistance des utilisateurs."""
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, user):
        """Sauvegarde un utilisateur."""
        if not hasattr(user, 'user_id'):
            user.user_id = self.next_id
            self.next_id += 1
        self.users[user.user_id] = user

    def get(self, user_id):
        """Récupère un utilisateur."""
        return self.users.get(user_id)

    def get_all(self):
        """Récupère tous les utilisateurs."""
        return list(self.users.values())

    def update(self, user_id, new_user_data):
        """Met à jour un utilisateur existant."""
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_user_data)
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        """Supprime un utilisateur existant."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
