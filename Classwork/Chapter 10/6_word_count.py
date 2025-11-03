print('\n') 

# ============================= You could always just have it fail 'silently', by just adding 'pass'. This way it just goes over it like it does not exist.  


from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass #so instead of giving it a thing to do when it fails, it just goes on. These gaurds are in place to make systems run without breaking 
    else:
        # Count the number of words in the file: 
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has exactly {num_words} words.")

filenames = ['ai_story_one.txt', 'ai_story_two.txt', 'ai_story_three.txt', 'ai_story_four.txt', 'alice.txt', 'FrankenStein.txt', "james_bond.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)


