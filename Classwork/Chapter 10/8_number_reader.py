print('\n') 

from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents) # so now it is a string type in the json file when you load it back into the file, it becomes a python list

print(numbers)
print(type(numbers)) 

print('\n') 