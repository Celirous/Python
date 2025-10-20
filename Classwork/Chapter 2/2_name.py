name = "aJ BelLrInger"
print(name.title())
print(name.upper())
print(name.lower())

print("\n")

first_name = "arno-johann"
last_name = "bellringer"
full_name = f"{first_name} {last_name}"
print(full_name.title())

print("\n")

first_name = "arno-johann"
last_name = "bellringer"
full_name = f"Hello {first_name} {last_name}. How are you doing?"
print(full_name.title())

print("\n") #makes a new line for you. A blank one

print("Python")
print("\tPython") # this is used to make a tab gap, the same way it would in a word doc
print("\n")
print("Languages:\nPython\nC\nJavaScript") # the \n is used to make a new paragraph basically. It makes like a small break for a new line
# you can also combine the two to get a nicer output. 
print("\n")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print("\n")

#we are now going to strip the gaps in a variables.
favourite_language = "    Python    "
print(favourite_language) 
print(favourite_language.rstrip()) #for righthand side 
print(favourite_language.lstrip()) #this is for lefthand side 
print(favourite_language.strip())  #this is for both sides
print("\n")

#we are now going to be removing prefixes and suffex
youtube_url = "https://www.youtube.com/dashboard"
print(youtube_url)
print(youtube_url.removeprefix("https://"))
print(youtube_url.removesuffix("/dashboard"))
print(youtube_url.removeprefix("https://").removesuffix("/dashboard"))
