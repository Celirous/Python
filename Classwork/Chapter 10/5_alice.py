print('\n') 

# ====================== We are going to work with many files now. 

    # we are making a function that can count words for us in many files 

from pathlib import Path

def count_words(filenames): #the reason we dont say path in the () is because we are going to add files in an array [] for the var filesnames
    """Count the words in the text files i tell you to"""

    try:
        contents = path.read_text(encoding="utf-8") #so this utf-8 is to tell the system in what way it needs to read the 1's and 0's to be able to read the info for humans
    except FileNotFoundError:                         # usually the utf-8 is done in background, the example is here to teach us about this 
        print(f"Sorry, the file you are looking: {filenames} for does not exist")
    else: #we are now going to count the words in the text file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filenames} has exactly {num_words} words.")

filenames = ['ai_story_one.txt', 'ai_story_two.txt', 'ai_story_three.txt', 'ai_story_four.txt', 'alice.txt', 'FrankenStein.txt', "james_bond.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)


