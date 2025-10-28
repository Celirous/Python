print('\n')

# 9.1 RESTAURANT

class Restaurant:
    """A class that models differnet Rastaurent types"""

    # CONSTRUCTOR
    def __init__(self, name, food_type):
        """Initialize name and food type attibutes for resturant class"""

        self.name = name
        self.food_type = food_type

    # METHODS
    def describe_restaurant(self):
        """Print disctiption of the restaurant"""

        print(f"The name of the restaurant is {self.name}. They serve {self.food_type} food here.")

    def open_restaurant(self):
        """Tells us if the restaurant is open"""

        print(f"{self.name} is open at 11am most days")

# INSTANTIATE INSTANT OF CLASS 

restaurant_1 = Restaurant("Joe's Pizzaria", "Pizza")

print(f"\nWelcome to {restaurant_1.name}. We serve {restaurant_1.food_type}.")
restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()

# MORE RESTAURANTS 
        
restaurant_2 = Restaurant("Mike's Kitchen", "Italian")
restaurant_3 = Restaurant("Hussar Gril", "Grilled")

print(f"\nWelcome to {restaurant_2.name}. We serve {restaurant_2.food_type}.")
restaurant_2.open_restaurant()
restaurant_2.describe_restaurant()

print(f"\nWelcome to {restaurant_3.name}. We serve {restaurant_3.food_type}.")
restaurant_3.open_restaurant()
restaurant_3.describe_restaurant()

print('\n')