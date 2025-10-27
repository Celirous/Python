print('\n') 



# def greet_user(): #we add the brackets because we might want to add more paramaters to this function (like extra data that gets passed into it)
#     """Display a simple greeting"""   # from what i understand this is called a doc string. This is a special note 
#     print('Hello')

# greet_user() #if you hover over this, it will show you the doc string from above, it shows you what you want the function should be, readability. 

print('\n') 

# def greet_user(): 
#     """Display a simple greeting"""
#     name = input(f'What is your name? ')
#     print(f'Hello there, it is good to meet you {name.title()}')

# greet_user()


# print('\n') 

def greet_user(username):
    """Display a simple greeting"""

    print(f'Hello, {username.title()}')

greet_user('Jessy')

print('\n') 

#paramater is the var in the functions
#arguments are what we pass into the paramater. In the example above we used "jessy" as the arguement and the "username" as the paramater 

