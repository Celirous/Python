print('\n')

#IMPORTING CLASSES

#IMPORTING A SINGLE CLASS
from car_module import Car

my_new_car = Car('audi', 'a4', 2024) #this is called instantiating a new car and storing it in the new variable my_new_car
print(my_new_car.get_descriptive_name())

print('\n') 

my_new_car.odometer_reading = 23800
my_new_car.read_odometer()

print('\n') 
my_new_car.odometer_reading = 21000
my_new_car.update_odometer()

print('\n') 
