print('\n') 
#IMPORT AN ENTIRE MODULE 

# import pizza_module  #when importing modules, do it at the top. 
# pizza_module.make_pizza(16 , 'peperoni', 'mushrooms')


# print('\n') 


# # IMPORTING SPECIFIC FUNCTION FORM A MODULE
# from pizza_module import make_pizza 

# make_pizza(18 , 'bacon', 'avo', 'feta')


print('\n') 

# USING AS TO GIVE A FUNCTION AN ALIAS

from pizza_module import make_pizza as mp #the 'as' here is what is giving it a temp new name 

mp(18 , 'bacon', 'avo', 'feta')

print('\n') 

# USING AS TO GIVE A MODULE AN ALIAS 

import pizza_module as p #the 'as' here is what is giving it a temp new name 

p.make_pizza(16 , 'peperoni', 'mushrooms') #we just had to specify the actual function of .make_pizza

print('\n')

#how to import all functions into a module 

from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n') 

#it is better to specify the functions you are importing so that you can always see what we imported. 

#always make your alias obvious. Dont be dumb

