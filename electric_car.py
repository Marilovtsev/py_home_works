class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное оптсание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит прбег машины в милях"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Устанавливает заданое значение на одометре.
        При рорытке обратной подкрутки изменение отклоянется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданым приращиванием."""
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля"""

    def __init__(self, battery_size=75):
        """Инициализирует атрибудты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """представляет аспекты машины, спецефические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для автомобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
