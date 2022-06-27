class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"First name: {self.first_name}"
              f"\nLast name: {self.last_name}"
              f"\nAge: {self.age}"
              f"\nEmail: {self.email}")


user_1 = User("John", "Shepard", 27, "shepard@normandy.com")
user_2 = User("Liara", "T'shoni", 435, "liara@normandy.com")
user_3 = User("Garrus", "Vakarian", 112, "garrus@normandy.com")

