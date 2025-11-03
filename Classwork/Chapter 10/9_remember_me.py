print('\n') 

from pathlib import Path
import json

# ============== EXAMPLE 1

# username = input("What is your name?")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")

#============= EXAMPLE 2

# path = Path('username.json')
# if path.exists(): #we are checking if the files are real, and then do something;
#     contents =path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}")
# else:
#     username = input("What is your name? ") # if they are not real, take the input here and make a file 
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")

# all of this is actually more for generating bug reports and stuff like that when things crash 

# ======================= EXAMPLE 3

# def greet_user():
#     path = Path('username.json')
#     if path.exists(): #we are checking if the files are real, and then do something;
#         contents =path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}")
#     else:
#         username = input("What is your name? ") # if they are not real, take the input here and make a file 
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# ====================== EXAMPLE 4

# def get_stored_username(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None
    
# def greet_user():
#     """Greet the user by name."""

#     path = Path('username.json')
#     username = get_stored_username(path)

#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# ====================== EXAMPLE 5

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()