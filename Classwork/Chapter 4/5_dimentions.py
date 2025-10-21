print('\n') 

# we are working with tuple (s) - these are lists that cannot be changed 

dimensions = (200, 50, 40, 1120)  #this is not a square bracket, because that is what defines a tuple 
print(dimensions[0])
print(dimensions[1])

print('\n') 

# # we will now try to change a value and you will see it wont work 

# dimensions[0] = 250 # <- this is the error now 

print('\n') 

for dimension in dimensions:
    print(dimension)

print('\n') 

# you can overwrite the tuple here as well (the individule items in this list cannot be overwritten but the whole thing can)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100) # when you do it like this, it does not reassign anything, but it does overwrite the ENTIRE list. 
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print('\n') 

