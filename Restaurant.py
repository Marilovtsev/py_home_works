class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        restourant_name = f"\n{self.restaurant_name}, {self.cuisine_type}"
        return restourant_name.title()
        # print(f"\n{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Today the {self.restaurant_name} with {self.cuisine_type} is open!")

    def check_number_served(self):
        print(f"Number served: {self.number_served}")

    def set_number_served(self, numbers):
        self.number_served = numbers

    # def increment_number_served(self, guests):
    #     self.number_served += guests


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 0

    def show_icecream(self):
        print(f"We can propose these ice-creams: {self.flavors}")


icecream_stand = IceCreamStand('Zori', 'Family cuisine')
print(icecream_stand.describe_restaurant())
icecream_stand.flavors = 'Vanilla', 'Cola'
icecream_stand.show_icecream()

# my_restaurant = Restaurant("Traktor Burger", "BBQ")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# restaurant = Restaurant("Buffet", "Family kitchen")
# nikos_info = Restaurant("Nikos", "Gastro & Bar")
# fat_goose_info = Restaurant("Fat Goose Pab", "Beer pub")
# pyana_vishnya_info = Restaurant("Pyana Vishnya", "Vine bar")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# nikos_info.describe_restaurant()
# fat_goose_info.describe_restaurant()
# pyana_vishnya_info.describe_restaurant()

# my_restaurant.number_served = 20
# my_restaurant.check_number_served()

# restaurant.set_number_served(15)
# restaurant.check_number_served()
#
# restaurant.increment_number_served(69)
# restaurant.check_number_served()
