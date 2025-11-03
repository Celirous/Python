print('\n') 

from pathlib import Path

path = Path('a_learning_python.txt')

# 1) Print entire file at once
contents = path.read_text(encoding='utf-8')
print(f'Entire file:')
print(f'{contents}')

print('\n') 

# 2) Print lines one by one 

lines = contents.splitlines()
print(f"Line by line:")
for line in lines:
    print(f"- {line}")

print('\n') 

# Replace words in text file

for line in contents.splitlines():
    new = line.replace("handle", "skip over")
    print(new)

print('\n')

# 3) Simplify the grabbing of info thing 

contents = path.read_text()
for line in contents.splitlines(): #the splitlines() gives you a list, you dont have to store the info in a var 
    print(line)
