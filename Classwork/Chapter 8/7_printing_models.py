print('\n') 
# Modifying a list in a function 

#### start woth some deigns that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")

# for completed_model in completed_models:
#     print(completed_model)


print('\n') 

# example 2 of actually using a function to edit the list 


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print('\n')

#so to make it easy yourself you can add a new list and everything but call on the same function 

# new_designs = ["hinge", 'lock', 'charger']
# print_models(new_designs, completed_models)
# show_completed_models(completed_models)

print('\n') 

#example 3 

# print("\nEXAMPLE 3")
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# copy_of_list = unprinted_designs[:] #so by adding that slice of the unprited_designs it will make a copy, so the orginal list wont be permanenetly updated. 

# print_models(copy_of_list, completed_models) #so copy_of_list is now the slice of unprinted_list[:] so it wont change the actual info inside of unprinted_designs list 

# show_completed_models(completed_models)
# print(f"Orginal List: {unprinted_designs}")
# print(f"Copy of original list: {copy_of_list}")


# SUMMARY:
# This program simulates a 3D printing process.
# It takes designs from the unprinted_designs list,
# prints each one, and moves them to the completed_models list.
# After all models are printed, it displays the completed models.