print('\n') 

from pathlib import Path

# ========= We are adding one thing to a list

# name = input("Give me your name:").strip() 

# path = Path('guest.txt')
# path.write_text(name, encoding='utf-8')

# print("Your name has been stored in guest.txt")

# =========== We are adding names to a list

# path = Path('b_guest.txt')

# print("Enter your 'q' when you want to quit")
# names = []

# while True:
#     name = input("What is your name: ")
#     if name == 'q':
#         break
#     else:
#         print(f"wecomeback {name}, been a while")
#         names.append(name + '\n')

# path.write_text(''.join(names), encoding='utf-8')
# print("Guest book updated")

# print('\n') 

#============= We are going to ask something and capture that info 

path = Path('programming_pole.txt')

respoonses = []

print("Enter 'q' any time to stop")
while True:
    anwser = input("Why do you like programming?: ")
    if anwser == 'q':
        break
    else:
        respoonses.append(anwser + '\n')

path.write_text(''.join(respoonses), encoding='utf-8')
print("Thank you! You responses have been saved.")

print('\n') 