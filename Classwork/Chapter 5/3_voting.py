# types of IF STATEMETNS 

print('\n')

#if they are older than 18, they can vote 
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you regestered?")
else: 
    print("Sorry, not yet")

print('\n')


age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print('\n') 

# if-elif-else chain (this is just an else if statement)

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#this is simple, there are just many ranges with many outputs 

print('\n') 

age = 45
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#if the age is over 65 you get the half off 

print('\n') 

# doing this wihtout the else at the end, omitting it 

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

print('\n') 


#testing mutiple conditions, they all need to be true for it to do

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#the reason we dont use elif statement is because it would stop after the first true comes out. So we want it to loop even when things are continuesly true 

print('\n') 


# using if statements for special items 


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")


print("\nFinished making your pizza!")

print('\n') 

# we are now checking if a list is NOT empty 

requested_toppings = []
if requested_toppings: #this is checking is there a value for 'requested toppings'. 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else: #if requested toppings are empty, it will print this lower part
    print("Are you sure you want a plain pizza?")


print('\n') 

# using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:  #this is actually quite simple, it is asking, do we have the requested in the available, if yes; print this, if not; do the else the else 
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

print('\n') 