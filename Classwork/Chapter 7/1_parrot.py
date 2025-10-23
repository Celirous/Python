print('\n') 

# input() functions 

#an input() function always outputs a sting 

# message = input("Tell me something, and I will repeat it back to you")
# print(message) #in the terminal it will output something like "....: []" and you can type next to the prompt message given, same as an alert() with JS but there is no popup


# ---------------------------------

# name = input("Please enter your name: ")
# print(f"\nHello, {name.title()}!")

#so you will enter info into the input and then it will output the print line on 12. 

# --------------------------------

# prompt = "If you share your name, we can prersonalize this message you see." 
# prompt += "\nWhat is your first name?" #you say += because it adds to prompt while keeping the previous set var for prompt 

# name = input(prompt)
# print(f"\nHello, {name.title()}!")

# print('\n')
# the reason we do this is so that we can just call the 'prompt' var here, it makes it so that you can grab
#  the prompt from anywhere and dont need to write out a huge string each time you ask the same question. 

# ----------------------------------- converting string (the data get from input() ) to interger (by using int() ) so that it can work and interact with each other

# age = input('How old are you?')
# print(age)

# print(type(age))  # ---- this is showing us the data type, because input() would always output a string 

# print('\n')

# # if age >= 18:
# #     print("Access granted") # --- this will break, because this is a string and not number type of data. So we need 
#                             #    to change the data type for it to interact with other things 

# age = int(age) # ----  this changes the data from a string to an interger 
# print(type(age))

# if age >= 18:
#     print("Access granted")

# # you will make the input within the var, you can just call the var whereever you need it 

# print('\n') 


# ---------------------------------


height = input("How tall are you?")
height = int(height) #because of this little part here 

if height >= 48:
    print(f"\nYou are tall enough to do this ride")
else: 
    print(f"\nYou'll be able to ride when you are a little older")

print('\n')

# ------------------ we are adding modulo operator, this gives you the decimal that is left over after this, 7/3 (this is twice and one is left)

