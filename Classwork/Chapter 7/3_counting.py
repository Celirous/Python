print('\n') 

# --------------------- while loops 

# current_number = 1
# while current_number <= 5:
#     print(current_number) #so here we are taking the current_number and adding one to it till it reaches 5. 
#     current_number += 1

# print('\n') 

# ----------------------------- 

# we are now going to make it so that the while loop ends when the user inputs the correct command 

# prompt = "\nTell me something, and I will repeat it back to you; "
# prompt += "\nEnter 'quit' to end the program: - " # this is += but because prompt var is now both these things,, now it can show in mutiple lines. 

# message = "\n" #this is blank because we need to update to "quit" from the input()

# while message != 'quit': #so if your message (which is the input() is the word quit then the while loop will end)
#     message = input(prompt)

#     if message != 'quit':
#         print(f"\nYour input: {message}") # we add this so that we can make it so that it does not output the word quit before ending the program 


print('\n') 

# -------------------- we are doing Flag 

# prompt = "\nTell me something, and I will repeat it back to you;"
# prompt += "\nEnter 'quit' to end the program: - "

# active = True # i think this is the flag, we just set it to true because that will make the game start. 
# while active: # this says, while the game is active (true) it will loop contineusly 
#     message = input(prompt)

#     if message == 'quit':
#         active = False #when the input (message var) becomes 'quit' the active will be set to false and the whole game will end 
#     else:
#         print(f"\nYour input: {message}")

# print('\n') 

# --------------------------- we are going to do a break (statement) to exit a loop, same as JS, just break out the loop

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break 
#     else: 
#         print(f"I'd love to go to {city.title()}")


# ------------------------- we are going to use continue in a loop 


# current_number = 0
# while current_number < 10: #the loop will run because 0 is in fact < than 0 - we add this so that it does not loop infinitly, just till 10
#     current_number += 1 #once current_number is in the loop, we increment with one in each loop 
    
#     if current_number % 2 == 0: #only once this is false will we print out the rest of the loop (what we are doing here is to check if it is an even number)
#         continue # this stops executing the rest of this code without breaking out of the loop, so this will be skipped until it is false 
#     print(current_number)

#this whole thing will only output odd numbers because the if statement here is true when it is devidable by 2 making it even numbers 

# if we want this to print even numbers we would say if current_number % 2 != 0




