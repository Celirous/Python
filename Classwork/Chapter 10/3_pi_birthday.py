print('\n') 

# Accessing 10 mil digit Pi and checking if you bday does show up 

from pathlib import Path

# path = Path('pi_ten_million.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

print('\n')

path = Path('programming.txt')
# path.write_text("I love programming and changing things!") #always remember that write_text overrides the content, always,
                                                            # so make a var to store the updated info in. 

contents = "I love programming\n"
contents += "I love digging in files too and updating things\n"
contents += "I also love breaking files\n"

path.write_text(contents)