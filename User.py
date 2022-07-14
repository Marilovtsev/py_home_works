"""Набор методов для создания User"""


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
