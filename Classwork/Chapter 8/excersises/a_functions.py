print('\n') 

# def favorite_book(book):
#     '''Gives you a sentance with fav book'''

#     print(f'My favourate book is: {book.title()}')

# favorite_book("Alice in wonderland")

# print('\n') 

# def make_shirt(size, print_text = "I am with stupid ----->"):
#     """Ordering a shirt to print"""

#     print(f'\nThank you for ordering a shirt')
#     print(f'Size of your shirt is: {size}')
#     print(f'The text on your shirt is: "{print_text}"')

# # Positional Argument
# make_shirt("Large", "Suck it shaun")

# # Keyword Argument 
# make_shirt(print_text="I am with Stupid --->", size="Medium")

# print('\n') 


# ----------------------- Cars 

def make_car(manufacturer, model, **car_info):
    """Storing car info"""
    car_info["manufacturer"] = manufacturer
    car_info['model'] = model 
    return car_info 


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)


print('\n') 