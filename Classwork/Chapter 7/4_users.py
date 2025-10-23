# ------------------------------------------ Moving items from one list to another 

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

# unconfirmed_users = ["alice", "brian", 'luke', 'candice']
# confirmed_users = [] 

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.

# while unconfirmed_users: # as long as there are items in the list of unconfirmed_user, run this 
#     current_user = unconfirmed_users.pop() #this will remove one item at a time from unconfirmed_user and give the new value to the new var current

#     print(f"\nVerifying new user: {current_user.title()}") #this is taking the removed user from var unconfirmed, and outputting that, which is the var current 
#     confirmed_users.append(current_user) # we are adding the removed user from unconfirmed, in var current into the end of the confirmed_users var 
#     print(f"\tUser: {current_user.title()} has been approved")
# # no we will display all confirmed users

# print(f"\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(f'\t{confirmed_user.title()}')

# print('\n') 


# ----------------------------- Removing all Instances of specific values from a list using .remove()


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# print('\n') 

# while 'cat' in pets:
#     pets.remove('cat')
#     print(f"Updating list: {pets}")
# print(f"\nFinal list: {pets}")

# print('\n') 

# --------------------------- filling a dictionary with user input

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True 

while polling_active: # as long as polling_active is True, this will loop 
    #prompt person name and mountain to climb
    name = input("\nWhat is your name?: ")
    response = input("Which mountain would you like to climb today?: ")
    # store the response in the dictionary 
    responses[name] = response #responses[name] is now the subcatagory within the dictionary. 
    #find out if anyone else is going to take the poll (it is looking for mutiple inputs)
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False # This would break the loop

#Polling is complete. Show results of poll 
print("\n--- Poll Results ---")
for name, response in responses.items(): #we say .items() because we are looking inside a dictionary 
    print(f"{name} would like to climb {response}")

print('\n') 

# Summary ----------------------------

# This program conducts a simple poll using a dictionary and a while loop.
    # It starts with an empty dictionary called responses to store people’s answers.
    # A flag variable (polling_active) controls the loop — it keeps running as long as polling is active.
    # Inside the loop:

        # The program asks each user for their name and the mountain they’d like to climb.
        # Each answer is stored in the dictionary, where the name is the key and the mountain choice is the value.
        # Then it asks if another person wants to take the poll. If the user answers “no,” the flag is set to False, stopping the loop.
    # After polling ends, the program prints the full list of poll results, showing each person and their chosen mountain.

