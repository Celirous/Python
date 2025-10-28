print('\n') 

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #this is a default value for all the car instantces.
                                  #So by default it would be 0, unless we add more

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""

        print(f"This car currently has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage): #so with this function we ae adding a function so that we can update the value of something
        """Update the Odometer with given value
        Reject the change if it attemps to rill the odometer back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    
# my_new_car = Car('audi', 'a4', 2024)
# print(f"I have a new car, it is a: {my_new_car.get_descriptive_name()}")
# my_new_car.read_odometer()

print('\n') 

my_new_car = Car('audi', 'a4', 2024)
print(f"I have a new car, it is a: {my_new_car.get_descriptive_name()}")

my_new_car.odometer_reading = 2588 #this gives the odometer_reading a new value directly
my_new_car.update_odometer(1900) #this does the same as above but it is a function now #now it cannot roll back due to the if statement in the function update_odometer
my_new_car.read_odometer()

print('\n') 

my_used_car = Car('subaru', 'outback', 2019)
print(f"I have a new car, it is a: {my_used_car.get_descriptive_name()}")


my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


my_used_car.increment_odometer(100)
my_used_car.read_odometer()


print('\n')


# SUMMARY:
# This program defines a Car class that stores basic information about a car,
# including make, model, year, and mileage (odometer_reading).
# It includes methods to:
#  - return a formatted name for the car,
#  - display the car’s current mileage,
#  - update the odometer safely (preventing rollback),
#  - and increment the mileage by a given amount.
# At the bottom, two Car objects are created (a new Audi and a used Subaru),
# their odometers are updated/incremented,
# and their details and mileage are printed.