class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Today the {self.restaurant_name} with {self.cuisine_type} is open!")


my_restaurant = Restaurant("Traktor Burger", "BBQ")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
