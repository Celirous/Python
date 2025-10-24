# print('\n') 

# people = input("How many people are in your dinner group? ")
# people = int(people)

# if people > 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready!")

# print('\n') 
# # ------------------

# prompt = "\nEnter a pizza topping (or 'quit' to stop): "

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break

#     print(f"I'll add {topping} to your pizza.")


# print('\n') 
# #------------------------


# prompt = "\nHow old are you? (type 'quit' to stop): "

# while True:
#     age = input(prompt)

#     if age == 'quit':
#         break

#     age = int(age)

#     if age < 3:
#         print("Your ticket is free!")
#     elif age <= 12:
#         print("Your ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")

# print('\n')

# # ---------------

# age = ""

# while age != "quit":
#     age = input("\nEnter age ('quit' to stop): ")
#     if age != "quit":
#         print(f"You entered age {age}.")

# print('\n')

# #--------------------


# active = True

# while active:
#     age = input("\nEnter age ('quit' to stop): ")
#     if age == "quit":
#         active = False
#     else:
#         print(f"You entered age {age}.")

# print('\n') 

# while True:
#     age = input("\nEnter age ('quit' to stop): ")
#     if age == "quit":
#         break
#     print(f"You entered age {age}.")

print('\n') 

# while True:
#     print("This loop will run forever!")

sanwich_order = ['tuna', 'ham', 'chicken', 'egg']
finished_sandwiches = []

while sanwich_order:
    current_sandwich = sanwich_order.pop()
    print(f'I made your {current_sandwich} sandwich')
    finished_sandwiches.append(current_sandwich)

print('\nAll sandwiches made:')
for sandwich in finished_sandwiches:
    print(sandwich.title())

print('\n') 


