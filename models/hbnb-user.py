#!/usr/bin/python3
"""Class User"""


class User:
    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return ("User(email='{}', first_name='{}', last_name='{}', "
                "password='{}')").format(self.email, self.first_name,
                                          self.last_name, self.password)

    def update_profile(self, first_name=None, last_name=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if password:
            self.password = password
