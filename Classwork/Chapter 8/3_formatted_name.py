# print('\n') 

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""

#     full_name = f'{first_name} {last_name}'
#     return full_name.title() 
# #so in this, we are only capturing.

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician) #we are printing it outside the funciton because the point of the function is to give the full_name var a value. So that you can take that full_name and do anything with that data 

# print('\n')

# # making an argument optional 

# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

print('\n') 
                                        # when you are adding a default value "middle_name=", then add it to the end of the arguements for the function 
def get_formatted_name(first_name, last_name, middle_name=''): #by making the middle_name as blank, it makes it so that there does not need to be a middle name for this to run. 
    """Return a full name, neatly formatted.""" 

    if middle_name: 
        full_name = f'{first_name} {middle_name} {last_name}'
    else: 
        full_name = f'{first_name} {last_name}'
        
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print('\n') 