name = "john"
print(f'Hello {name}, do you want to learn some Python today?')

print('\n')

print(name.upper())
print(name.lower())
print(name.title())

print('\n')

name = "franklin d. roosevelt"
print(f"{name.title()} once said, 'The only thing we have to fear is fear itself'")

print('\n')

famous_person = "steve jobs"
famous_quote = "The only way to do great work is to love what you do"

print(f'{famous_person.title()} once said, "{famous_quote}"')

print('\n')

favourite_name = "    Jannet    "
print(favourite_name) 
print(favourite_name.rstrip()) #for righthand side 
print(favourite_name.lstrip()) #this is for lefthand side 
print(favourite_name.strip())  #this is for both sides

print("\n")


file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))

print('\n')

print(5 + 3)
print(10 - 2)
print(16 / 2)
print(4 * 2)

print('\n')

fav_num = 17
info_message = "My favourite number is:"
print(f'{info_message} {fav_num}')

print('\n')
