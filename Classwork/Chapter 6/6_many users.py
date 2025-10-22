print('\n') 

#we are going to make dictionaries within dictionaries 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
# in this case, the key() is the username (aeinstein/mcurie) and the value() is the things within the user info (user_info)

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t- Full Name: {full_name.title()}")
    print(f"\t- Location: {location.title()}")


print('\n') 


# -------------------- CHATGPT summary of code 

# This program demonstrates how to use dictionaries within dictionaries in Python.
#   The main dictionary, users, stores information about multiple people.
#       Each key (like 'aeinstein' or 'mcurie') represents a username.
#       Each value is another dictionary containing details such as first name, last name, and location.
#   A for loop goes through all key–value pairs in users.
#       It extracts the username (key) and the nested dictionary (user_info).
#       Then it formats and prints the person’s full name and location, with proper capitalization.
# Essentially, it’s a small program that shows how to organize and access complex data structures using nested dictionaries and loops.