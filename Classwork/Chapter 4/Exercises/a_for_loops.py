print('\n') 
fav_pizzas = ["Bacon, Avo & Fetta", "Pepperoini", "Chicken Mayo"]

for fav_pizza in fav_pizzas: 
    print(f"I really like {fav_pizza} pizza")

print(f'\nSometimes I prefer {fav_pizza}, other times not')
print("\nI enjoy trying different toppings and flavours.")
print("Each one has something special about it.")
print("I really love pizza!")

print('\n') 


pet_animals = ["Dog", "Cat", "Hamster", "Rabbit"]

for pet_animal in pet_animals:
    print(f"{pet_animal}s, they make great pets")

print("\nAll of these animals are friendly and love being around people.")
print("Any of them would make a wonderful pet!")

print('\n')


numbers = list(range(1, 21))
print(numbers)
for number in numbers: 
    print(number)

print('\n') 


one_hundred_thousand = list(range(1 , 100_001))

print(f'{min(one_hundred_thousand)}')
print(f'{max(one_hundred_thousand)}')
print(f'{sum(one_hundred_thousand)}')

print('\n') 


numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)


print('\n') 

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print('\n') 
# --- Shorter versio of this 

for number in range(1 , 11):
    print(number ** 3)

print('\n')

cubes = [number **3 for number in range(1, 11)]
print(cubes)

print('\n') 


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'{players}')

print(f'\nThe first 3 players are: {players[:3]}') #this is for the first 3 
print(f'The middle 3 players are: {players[1:4]}') #this is middle 3
print(f'The last 3 players are: {players[2:]}') #this is the last 3 

print('\n') 


print(fav_pizzas)

friend_pizzas = fav_pizzas[:]

fav_pizzas.append("Man & Cheese")
for fav_pizza in fav_pizzas:
    print(f'This is an updated verson of my favs, they are: {fav_pizza}')

print('\n') 

friend_pizzas.append("BBQ Chicken")
for friend_pizza in friend_pizzas:
    print(f'My friends fav pizzas are: {friend_pizza}')

print('\n')