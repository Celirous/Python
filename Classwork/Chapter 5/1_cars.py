print('\n') 

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())


#so we made it here that the whole list is going to be outputted, but if the list contains the value "bmw" it should output it in upppercase if not, have it with a normal tittle format 

print('\n') 

# Checking for equality in the var list so "=" assigns the value to something "==" asks if it is the same value 

car = "bmw"
print(f"Is the car a bmw?: {car == 'bmw'}")

car = "audi"
print(f"Is the car a bmw?: {car == 'bmw'}")

print('\n') 

# Checking is case sensitive 

car = "Audi"
print(f'Is the car an Audi?: {car == "Audi"}')
print(f'Is the car an Audi?: {car == "audi"}') 

# if it is not important that it is case sensitive you can just make it how you want it, like a user name, if they have mutiple 

print(f'Is the car an Audi?: {car.lower() == "audi"}') #this is not a permanent change of car, it is just in this check that it would be lower case 

print('\n') 


# checking for inequality 

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the achovies")


print('\n') 

