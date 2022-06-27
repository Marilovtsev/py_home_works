class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"First name: {self.first_name}"
              f"Last name: {self.last_name}"
              f"Age: {self.age}"
              f"Email: {self.email}")
