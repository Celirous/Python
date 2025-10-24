print('\n')

# person = {
#     'first_name': 'john',
#     'last_name': 'doe',
#     'age': 25,
#     'city': 'cape town',
# }

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])


print('\n') 


# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'mississippi': 'united states',
# }

# for river, country in rivers.items():
#     print("The " + river.title() + " runs through " + country.title() + ".")

# print("\nRivers:")
# for river in rivers.keys():
#     print(river.title())

# print("\nCountries:")
# for country in rivers.values():
#     print(country.title())


print('\n') 

games = {
    'minecraft': {'type': 'sandbox', 'players': '1-100'},
    'fortnite': {'type': 'battle royale', 'players': '100'},
    'rocket league': {'type': 'sports', 'players': '1-8'},
}

for game, info in games.items():
    print("\nGame: " + game.title())
    print("Type: " + info['type'])
    print("Players: " + info['players'])

print('\n') 
