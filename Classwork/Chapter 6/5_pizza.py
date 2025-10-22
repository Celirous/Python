print('\n') 

# we are dealing with lists inside of dictionaries

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'], #so the keys() here are crusts and toppings 
}                                           # the values() are think and mushrooms/ extra cheese 

print(f'You ordered a {pizza['crust']}-crust pizza with the follwing toppings:')

for topping in pizza['toppings']:
    print(f'\t-{topping}')

print('\n') 


#so now we have lists within a dictionary, we are going to loop through it now 

favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items(): #so the keys() here are names. # the values() are the languages 
    print(f"\n{name.title()}'s favorite leangues are:")
    for language in languages:
        print(f'\t{language.title()}')
 # name, languages and language are all temp variables that we make for these for loops 
print('\n') 

