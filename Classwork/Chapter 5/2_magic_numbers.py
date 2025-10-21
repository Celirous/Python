print('\n') 
#number comparisons 

age  =  18
print(f"Is the person 18 years old? {age == 18}")

print('\n') 

age = 19 
print(f"Is the person older than 21 years old? {age > 21}")
print(f"Is the person older than or 21 years old? {age >= 21}")
print(f"Is the person younger than 21 years old? {age < 21}")

print('\n') 

#checking mutiple conditions 
# 1) using "and" operator 

age_0 = 22
age_1 = 18

admission = age_0 >= 21 and age_1 >= 21 

print(f'Are both people allowed in the club? {admission}') #this will say false because they are both not older than 21

print('\n') 

age_0 = 22
age_1 = 24

admission = age_0 >= 21 and age_1 >= 21 

print(f'Are both people allowed in the club? {admission}') #this will say true because they are both older than 21

print('\n') 

# using "or" operator 

age_0 = 22
age_1 = 18

admission = age_0 >= 21 or age_1 >= 21 # is either of them older than 21? 

print(f'Are both people allowed in the club? {admission}') #this will say true because at least one of them is older than 21 

print('\n') 

# we are checking is there something in a list. using "in" operator 

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print(f"Should we add mushrooms?: {'mushrooms' in requested_toppings} because it was in the list") # this would say true because there are in fact mushrooms 
print(f"Should we add pepperoni?: {'pepperoni' in requested_toppings} because it was not in the list") #this would say false because there are no peperoni in the list 

print('\n') 

# we are checking if something is NOT in the list 

banned_users = ['andrew', 'carolina', 'david']
user = "marie"

if user not in banned_users:
    print(f'{user.title()}, you can post a personse if you wish!')


print('\n') 

banned_users = ['andrew', 'carolina', 'david']
user = "andrew"

if user not in banned_users:
    print(f'{user.title()}, you can post a personse if you wish!')
else:
    print(f"You are no longer authorised to post anything, {user.title()}")


print('\n')


#boolean expressions 

game_active = True # this is us setting rules in something 
can_edit = False
