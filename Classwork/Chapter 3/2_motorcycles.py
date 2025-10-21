motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print('\n')

# motorcycles[0] = 'ducati' #this is updating index 0 (honda) to the new one 'ducati'
# print(motorcycles)

# print('\n')

#we are going to add things to the list 

    # we are going to use .append, this adds it to the end 


motorcycles.append('ducati')
print(motorcycles)

print('\n')

    # we will now insert into the array position here 

motorcycles.insert(4, 'kawasaki')
print(motorcycles)

print('\n')

    # we will now remove from the list using 'del', which works like delete 

del motorcycles[0] # you need to specify which index position we are deleteing
print(motorcycles)

print('\n')

    # you can also use the popped method, removed the last index postion 

popped_motorcycle = motorcycles.pop()
print(f"The bike we removed was = {popped_motorcycle.title()}")
print(motorcycles)

print('\n')

    # as a note, you can popped any item in the list by specifying what you want to remove by specifying the index postition 

popped_motorcycle = motorcycles.pop(2)
print(f"The bike we removed was = {popped_motorcycle.title()}")
print(motorcycles)

print('\n')

    # we can also .remove things by their value 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawasaki']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print('\n')

    # you can also use the .remove method to working with a value 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)



too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print('\n')


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawasaki']

for bike in motorcycles:
    print(bike.title())


