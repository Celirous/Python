print('\n') 

#we are still busy with input()
# ------------------ we are adding modulo operator, this gives you the decimal that is left over after this, 7/3 (this is twice and one is left) using the "%" symbol

number = int(input("Enter a number, and I'll tell you if it is even or odd: "))

if number % 2 == 0: #we are basically asking if the number is devidable by 2 without leaving anything over. Using modulo "%"
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")

print('\n') 