# dictionary 

print('\n')

alien_0 = {'color': 'green', 'points': 5 }

print(alien_0['color'].title())
print(alien_0['points'])

print('\n') 

new_points = alien_0['points']
print(f'You just earned {new_points} points')

#this names it so that you can access the "points" with a new variable 
print('\n') 

alien_0 = {'color': 'green', 'points': 5}
print(f'This is the orignoal dictionary: \n{alien_0}')

print('\n')  

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f'\nThe new dictionary is: {alien_0}')

#here we added more info to the alien_0 dictionary 

print('\n')

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# making it from blank, this is helpful for storing "points" for a player. 

print('\n') 

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}')

#this is modifying the values of things in dictionaries 

print('\n')


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original 'x' position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1 #this is a temp var to incriment the x posistion 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'The new "x" postition: {alien_0["x_position"]}')

print('\n') 

# ----------------------------------------

# we are now going to remove 'key points' 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print('\n') 



