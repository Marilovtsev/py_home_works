class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")


my_restaurant = Restaurant("Traktor Burger", "BBQ")

my_restaurant.describe_restaurant()
