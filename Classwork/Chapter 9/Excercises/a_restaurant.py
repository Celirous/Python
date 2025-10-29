print('\n')

# 9.1 RESTAURANT

class Restaurant:
    """A class that models differnet Rastaurent types"""

    # CONSTRUCTOR
    def __init__(self, name, food_type):
        """Initialize name and food type attibutes for resturant class"""

        self.name = name
        self.food_type = food_type
        self.number_served = 0

    # METHODS
    def describe_restaurant(self):
        """Print disctiption of the restaurant"""

        print(f"The name of the restaurant is {self.name}. They serve {self.food_type} food here.")

    def open_restaurant(self):
        """Tells us if the restaurant is open"""

        print(f"{self.name} is open at 11am most days")

    def amount_served(self, served):
        """This tells us how many clients the restaurant served today"""

        self.number_served = served
        print(f"Today we managed to serve {self.number_served} people")

    def increment_people(self, new_clients):
        """This is used to add one person that was served each time"""

        self.number_served += new_clients
        print(f"We have served few people, bringing today's total to {self.number_served}")

# INSTANTIATE INSTANT OF CLASS 

restaurant_1 = Restaurant("Joe's Pizzaria", "Pizza")

print(f"\nWelcome to {restaurant_1.name}. We serve {restaurant_1.food_type}.")
restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()
restaurant_1.amount_served(84)

# MORE RESTAURANTS 
        
restaurant_2 = Restaurant("Mike's Kitchen", "Italian")
restaurant_3 = Restaurant("Hussar Gril", "Grilled")

print(f"\nWelcome to {restaurant_2.name}. We serve {restaurant_2.food_type}.")
restaurant_2.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.amount_served(128)

print(f"\nWelcome to {restaurant_3.name}. We serve {restaurant_3.food_type}.")
restaurant_3.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.amount_served(158)
restaurant_3.increment_people(5)

print('\n')