print('\n') 

# =========================================
# IMPORTING MULTIPLE CLASSES FROM A MODULE

# from car_module import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# print('\n')

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

print('\n') 

# =========================================
#IMPORTING AN ENTIRE MODULE 

# import car_module

# my_mustang = car_module.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# print('\n') 

# my_leaf = car_module.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

print('\n') 

# =========================================
#IMPORTING ALL CLASSES FROM A MODULE 

from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

print('\n')

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print('\n') 

# =========================================

