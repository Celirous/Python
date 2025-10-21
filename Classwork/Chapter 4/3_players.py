# slicing of lists 
print('\n') 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # this is selecting the positions of the index posistions. In this case it will be index 0, 1 and 2 (not including 3) and then outputting it

print('\n')

print(players[1:4]) # you can have it start and end anywhere we indicate, here it is 1, 2 and 3 not including 4
print(players[:4]) #if you leave the first value empty, it will know to start at the beggining of the list
print(players[2:]) #if you leave the last value empty, it will know to go from where we start to the end of the list 
print(players[-3:]) #same as with others, if you add a "-" to index position, it will start from the back (and in this case, till the end)
print('\n') 

# looping through a slice 

print("Here are the first three players on my team:")
for player in players[:3]: #we are slicing from beggining of array to the end of it  
    print(player.title())

print('\n') 

