print('\n') 

# passing an Arbitrary number of Arguments

def make_pizza(*toppings): #the * here means there can be any amount of arguements and it will be safed as a tuple// remember a tuple is like a list but cannot be updated, only completely changed
    """Print the list of toppings that been requested"""
    print(toppings) 

make_pizza('pepperoni') #on the output ehre it will show ('pepperoni',), the comma in the brackets is to show it is a tuple type of data
make_pizza('mushrooms', 'green peppers', 'extra cheese') #because we added the single '*' up top it can be as many as we want - using one '*' you making a tuple


print('\n') 

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")

    for topping in toppings:
        print(f'- {topping}')
    
make_pizza('pepperoni') #on the output ehre it will show ('pepperoni',), the comma in the brackets is to show it is a tuple type of data
make_pizza('mushrooms', 'green peppers', 'extra cheese') #because we added the single '*' up top it can be as many as we want - using one '*' you making a tuple

print('\n') 

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n') 

def build_profile(first, last, **user_info): #by adding the two '**' we are making a dictionary and not a tuple 
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') #all the info after "last" would continuesly build the dictionary. 
                                                                                        #we are now adding the key values with the 'location=' and stuff. 
print(user_profile)

print('\n') 