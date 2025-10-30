print('\n') 

## READING CONTENTES OF A FILE 

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()


lines = contents.splitlines() # Accessing files's lines
for line in lines:
    print(f" - {line}")

print('\n') 

# working with a file's content

lines = contents.splitlines()
pi_string = ''

for line in lines:
    # pi_string += line #so if we out put this, it will output like this - 3.1415926535    8979323846    2643383279
    pi_string += line.lstrip() #by adding the .lstrip it will output like this - 3.141592653589793238462643383279

print(pi_string)
print(len(pi_string))

print('\n')