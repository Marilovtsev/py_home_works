class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFirst name: {self.first_name}"
              f"\nLast name: {self.last_name}"
              f"\nAge: {self.age}"
              f"\nEmail: {self.email}")

    def greet_user(self):
        print(f"\nWelcome to the Normandy, {self.first_name} {self.last_name}!"
              f"\nYour personal email for communication: {self.email}"
              f"\nAt the time of registration in the ship's system, your age is {self.age} years."
              f"\nLogin attempts: {self.login_attempts}")

    def increment_login_attempts(self, number):
        self.login_attempts = number

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)

    def show_privileges(self, privileges):
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять пользователей',
                           'разрешено банить пользователей']
        print(self.privileges)


admin = Admin("John", "Shepard", 27, "shepard@normandy.com")
admin.show_privileges(privileges=())

# user_1 = User("John", "Shepard", 27, "shepard@normandy.com")
# user_2 = User("Liara", "T'Soni", 435, "liara@normandy.com")
# user_3 = User("Garrus", "Vakarian", 112, "garrus@normandy.com")

# user_1.describe_user()
# user_2.describe_user()
# user_3.describe_user()

# user_1.greet_user()
# user_2.greet_user()
# user_3.greet_user()

# user_1.login_attempts = 1
# user_1.greet_user()

# user_1.reset_login_attempts()
# user_1.greet_user()
