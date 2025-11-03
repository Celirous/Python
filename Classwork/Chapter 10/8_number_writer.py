print('\n') 

# ========================================== We can store data using JSON. using json.dumps() and json.loads()

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json")
content = json.dumps(numbers) #originally it was a python list, by using the dump method, it changes the file type to json and makes it a string 
                            
path.write_text(content) 
print(type(numbers))

