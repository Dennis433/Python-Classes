
class Car:
    '''A simple attempt to model a Car'''
    def __init__(self, make, model, year):
        '''initialize the name and the model'''
        self.name = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.name} {self.model}"
        return long_name.title()

    def auto_drive(self):
        '''stimulate the car to drive in response to a command'''
        print(f'{self.model} is now auto driving')

    def auto_reversing(self):
        '''stimulate the car to reverse in response to a command'''
        print(f'{self.model} has just automatically reversed')

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class Eletric_Car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        '''Then initialize attributes specific to an electric car.'''
        self.battery = Battery()



my_tesla = Eletric_Car('Tesla', 'Model S', 2019)
print(f'This is a {my_tesla.get_descriptive_name()}')
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()