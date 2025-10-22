print('\n') 

#looping through dictionaries 

#looping through all key value parts: 

user_0 = {
'username': 'efermi', #so the 'username' is the key and the 'efermi' is the value 
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items(): #the .items() is grabbing all the key values. You dont have to use "key" and "value", you can use anything, like "user" and "email" 
    print(f'Key: {key}') #this is called "key", because that is what we set as the temp value in the for loop a the beginning 
    print(f'Value: {value}')

print('\n') 

# we will be doing the same but with a differnet data set 

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s fav language is {languages.title()}")

#again, this was to loop through everything here

print('\n') 

# now we are going to only loop the 'keys'

for name in favorite_languages.keys():
    print(name.title())

print('\n') 

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}')

print('\n') 

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

print('\n') 

# we are now going to loop through the keys but in a specific order

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking our poll.')

print('\n') 


# we are now going to loop through the values() not the keys 

favorite_languages = {
'jen': 'python', #again, the values are the second set of info, in this case it would be the languages 
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been selected for the poll:")
for language in favorite_languages.values():
    print(f'\t-{language.title()}')

print('\n') 

print(f'Unique vales:')

for language in set(favorite_languages.values()): #if you use the set(), it wont bring up doubles, it only counts the unique values, so if python came up more than once, it will only ouput once 
    print(f'- {language.title()}')

print('\n') 