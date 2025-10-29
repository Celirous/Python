print('\n') 

# ----------------------------------------------------------------------
            # Main class, Car


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        """Add the given amount to the odometer reading."""

        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Simulate filling up gas tank"""
        print("Filling up a gas tank")


# ---------------------------------------------------------------------------------- 

# we are making an extra class called battery 

class Battery:
    """A Simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40): #always place default values at the end, it is because we dont need to pass info in
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nInside Battery Class: This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print((f"This car can go about {range} miles on a full charge"))


#----------------------------------------------------------------------------

            # Subclass ElectricCar


# WE ARE DOING A SUBCLASS NOW, a new class within the car class. CALLED CHILD CLASS


class ElectricCar(Car): #so with the capital C in car we are accessing the class of Car here .
    """Represent aspects of a car, specific to electric vehicles
    Then initialize attributes specific to an electric car."""

    def __init__(self, make, model, year): #this was auto filled when i pressed enter. It can tell we are taking from Car class. 
        super().__init__(make, model, year) #super() here refers you to the parent class in this case it is Car. the __init__() here is making it so that the subclass gets all the info from the parent class
        self.battery_size = 40
        self.battery = Battery()

    # Defining attributes and medthods for child class
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nInside Subclass: This car has a {self.battery_size}-kWh battery")

    # Overiding Methods from parent class
    def fill_gas_tank(self): #the function has the same name as the parent class, but we changed what it does 
        """Electric cars dont have gas tanks"""
        print("This car does not have a gas tank")


# CREATE INSTANCE FOR CHILD/SUB CLASS 

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Defing attributes and medthods for child class
my_leaf.describe_battery()

print('\n') 

#Overiding methods from parent class 
my_leaf.fill_gas_tank()

my_leaf.battery.describe_battery()

my_leaf.battery.get_range()

print('\n')