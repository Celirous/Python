print('\n') 

from a_restaurant import *

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