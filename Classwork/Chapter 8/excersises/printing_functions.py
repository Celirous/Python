print('\n') 

def build_profile(first, last, **user_info): #by adding the two '**' we are making a dictionary and not a tuple 
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') #all the info after "last" would continuesly build the dictionary. 
                                                                                        #we are now adding the key values with the 'location=' and stuff. 


print('\n') 

def make_car(manufacturer, model, **car_info):
    """Storing car info"""
    car_info["manufacturer"] = manufacturer
    car_info['model'] = model 
    return car_info 


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print('\n') 