#we are doing more dictionaries, getting more and more info stored in them 
print('\n') 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
languages = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is: {languages}")

print('\n') 

# we can use "get()" to access values, this helps to look for something if we are not 100% sure where the index is. 

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# This results in a traceback, showing a KeyError:

# Traceback (most recent call last):
#   File "alien_no_points.py", line 2, in <module>
#       print(alien_0['points'])
#           ~~~~~~~^^^^^^^^^^ 
# KeyError: 'points'

point_value = alien_0.get('points', 'No point value assigned') #so we are setting what we are looking for "points" and if they cant find it, "No point value assigned", if you leave it blank, it would just output 'none' 
print(point_value)

#you can also just not make a new var like this: 

print(alien_0.get('points', 'No point value assigned'))

print('\n') 

# Looping through dictionaries 

