print('\n') 

# we are going to make lits inside of dictionaries 

alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'slow'}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'slow'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#this of there being different alien enemies in your game, so we want to define them differently. 

print('\n') 

#we are going to make a blank alien list and then add alients using a for loop here

aliens = []

for alien_number in range(10):
    new_alien = {'name': 'Jerron', 'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(f'{alien}')
print('\n...')

print(f'\nTotal number of aliens: {len(aliens)}') #the len here means length, so we are checking the length of the dictionaries 

print(f'\n{aliens}')

print('\n')

#we are now going to change values 

aliens = []

for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[3:6]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)

print('\n') 