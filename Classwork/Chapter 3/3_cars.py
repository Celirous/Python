# we are doing the sort method now 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # it will sort to alphabetical order, permanently. 
print(cars)

print('\n')

    # you can do it in a reverse order too. 

cars.sort(reverse=True)
print(cars)

print('\n')

# you can do a temporarily sorting it by using .sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"1) Here is the original list: \n{cars}")
print("\n")
print(f"2) Here is the sorted list: \n{sorted(cars)}")
print(f"3) Here is the sorted list in reverse: \n{sorted(cars, reverse=True)}")

print('\n')

# Getting the lengh of a list using the len method (meaning)

print(f"Length of car list = {len(cars)}") 

print('\n')