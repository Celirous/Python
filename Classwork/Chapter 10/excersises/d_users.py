print('\n') 

from pathlib import Path
import json

def get_stored_user(path):
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    else:
        return None
    
def get_new_user(path):
    name = input("What is your name?: ")
    age = input("What is your age?: ")
    data = {'name': name, 'age': age}
    path.write_text(json.dumps(data), encoding='utf-8')
    return data

def greet_user():
    path = Path('d_user_data.json')
    user_data = get_stored_user(path)
    if user_data:
        name_check = input("What is your name?: ")
        if name_check.strip() == user_data['name']:
            print(f"Wecolme back, {name_check}!")
        else:
            print("New user detected.")
            user_data = get_new_user(path)
            print(f"Nice to meet you, {user_data['name']}!")
    else:
        user_data = get_new_user(path)
        print(f"I'll remember you next time, {user_data['name']}")

greet_user()
