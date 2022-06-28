class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное оптсание"""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())