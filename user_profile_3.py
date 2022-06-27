class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"\nFirst name: {self.first_name}"
              f"\nLast name: {self.last_name}"
              f"\nAge: {self.age}"
              f"\nEmail: {self.email}")

    def greet_user(self):
        print(f"\nWelcome to the Normandy {self.first_name} {self.last_name}!"
              f"\nYour personal email for communication: {self.email}"
              f"\nAt the time of registration in the ship's system, your age is {self.age} years."


user_1 = User("John", "Shepard", 27, "shepard@normandy.com")
user_2 = User("Liara", "T'shoni", 435, "liara@normandy.com")
user_3 = User("Garrus", "Vakarian", 112, "garrus@normandy.com")

# user_1.describe_user()
# user_2.describe_user()
# user_3.describe_user()

