"""Набор классов для заполнения профиля User"""

from User import User


class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=''):
        self.privileges = privileges

    def show_privileges(self):
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять пользователей',
                           'разрешено банить пользователей']

        for priveleg in self.privileges:
            print(priveleg)
