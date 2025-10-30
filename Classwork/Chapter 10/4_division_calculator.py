print('\n')


# Handeling the ZeroDivisionError Exception 

# print(5/0) #impossible math. 
# but you can get around this 

# you can use something called 'try-except Blocks 

try:
    print(5/0)
except ZeroDivisionError: #from what i understand it is used so the system rather tells you it is not working rather than crashing python 
    print("You can't devide by zero!")

print('\n') 

# this is also usefull if you dont want a system to crash if it cannot locate a file, rathe 'stop it' than break it all. 

# from pathlib import Path

# path = Path('pi_ten_million.txt') #this wont give an error because it is found
# # path = Path('pi_one_million.txt') #this will give an error but the except will catch it for us because it does not exist anywhere

# #this is to prevent crashes
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print("Sorry - {path} wasn't found. Make sure the file is in the program folder")
# else: # you can have like 'else' gaurds incase you update something and it works now so that the saftey measure is still there just in case
#     # lets have it count the words in the file if it is there. 
#     words = contents.split()
#     num_words = len(words)
#     print(f'The file {path} has about {num_words} words.')


# #so we can use Exceptions to Prevent Crashes. This is how you keep systems from going down completely 

# print("Give me two number, and I'll devide them.")
# print("Enter 'q' to quit")

# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond Number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)
#  this is a brasic calculator. it will break the moment we go 0 / 0. 

# ELSE BLOCKS 
# we are going to use an else block to make it so that it will rather give an error than stop working 

# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond Number: ")
#     if second_number == 'q':
#         break
#     try: #so by saying try we are asking it to do something else instead of breaking
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You cant devide by 0!")
#     else:
#         print(answer)
    


# ====================== We are going to work with many files now. 

    # we are making a function that can count words for us in many files 

# from pathlib import Path

# def count_words(filenames): #the reason we dont say path in the () is because we are going to add files in an array [] for the var filesnames
#     """Count the words in the text files i tell you to"""

#     try:
#         contents = path.read_text(encoding="utf-8")
#     except FileNotFoundError:
#         print(f"Sorry, the file you are looking: {path} for does not exist")
#     else: #we are now going to count the words in the text file
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path} has exactly {num_words} words.\n")

# filenames = ['ai_story_one.txt', 'ai_story_two.txt', 'ai_story_three.txt', 'ai_story_four.txt']
# for filename in filenames:
#     path = Path(filename)
#     count_words(path)


# ============================= You could always just have it fail 'silently', by just adding 'pass'. This way it just goes over it like it does not exist.  

