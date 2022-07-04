class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Today the {self.restaurant_name} with {self.cuisine_type} is open!")

    def check_number_served(self):
        print(f"Number served: {self.number_served}")


my_restaurant = Restaurant("Traktor Burger", "BBQ")
restaurant = Restaurant("Buffet", "Family kitchen")
nikos_info = Restaurant("Nikos", "Gastro & Bar")
fat_gouse_info = Restaurant("Fat Gouse Pab", "Beer pub")
pyana_vishnya_info = Restaurant("Pyana Vishnya", "Vine bar")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# nikos_info.describe_restaurant()
# fat_gouse_info.describe_restaurant()
# pyana_vishnya_info.describe_restaurant()
