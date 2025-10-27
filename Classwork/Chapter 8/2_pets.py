#inputting mutiple arguments into set paramaters. The order of what you write out your paramaters, that is the order that your arguments will be read. 
# in this example we put animal_type and then pet_name. So when we call the function and input arguements, it has to be in order of paramaters. 

# def describe_pets(animal_type, pet_name):
#     """Display infomation about pets"""

#     print(f'\nI have a {animal_type}')
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pets('hamster', 'harry')
# describe_pets('cat', 'ghato') #the order is super important here, look at how we made the function, so if we add it in the wrong order, it will display wrong 

# describe_pets(pet_name ='susan', animal_type='fish',) #when you make a keyword arugement like this, the order is less important as we are updating the actual paramaters 

# print('\n') 

def describe_pets(pet_name, animal_type='dog'): #by adding the arguement of dog here, that sets a default value for animal_type. So it will always be dog here unless we specify otherwise 
    """Display infomation about pets"""

    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pets('willie') #we dont have to say pet_name= because we are typping in order, so 'willy' argument would go into the pet_name paramater anyway because it is first in the function anyway

describe_pets(pet_name='harry', animal_type='hamster') #because we have changed the animal type, it will now update when the function is being called 

# print('\n') 

# #we will now show how we can have arguemnts defined in differnet ways 

# # A dog named Willie.
# describe_pets('willie')
# describe_pets(pet_name='willie')
# # A hamster named Harry.
# describe_pets('harry', 'hamster')
# describe_pets(pet_name='harry', animal_type='hamster')
# describe_pets(animal_type='hamster', pet_name='harry')

print('\n')

#we can force an error message that will help us to find where the issue is. 
# describe_pets() #it says in the teminal saying that we need to add the pet name. This is because we have defined animal_type as dog 

