print('\n') 

"""A Set of classes that can be used to represent electric cars"""

# we are importing a module into a module 

from car_module import Car

# =================================================================
            # Battery Class
# =================================================================

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

# =================================================================
            # Electric Car Class
# =================================================================

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        
        super().__init__(make, model, year)
        self.battery = Battery()


my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

print('\n') 

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print('\n') 
