# making numbered lists 
    # using range() function 

for value in range(1,5): #this will be digits 1-4 as it does not include the 5. 
    print(value)

print('\n') 

for value in range(0, 6): #this will include 5 now and start at 0
    print(value)

print('\n') 

#we want to now take the range and make it a list 
# we used RANGE() to make a list of numbers 
numbers = list(range(1,6))
print(numbers)

print('\n') 

# we will make this range in places of 2, "ste size"

even_numbers = list(range(2, 11, 2))        # so this will start at 2, end before 11 and it will do it in "steps of" 2 
print(even_numbers)

print('\n') 


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# over here we make it so that we start with an empty square and then we loop through it from 1 to 10  then we are kaing that and making it to the power of 2 and then outputting that 

print('\n') 

squares = []
for value in range(1, 11):
    squares.append(value**2) #this is a better way to do the same thing as up top

print(squares)

print('\n') 

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'The max digit on this is {max(digits)}')
print(f'The min digit on this is {min(digits)}')
print(f'The sum of the digits are, {sum(digits)}')

print('\n')

# we will print out each item in the loop and have it made to the power of 2 

squares = [value**2 for value in range(1, 11)] #so here we are making a blank list, in there each item needs to **2, what is each item you asK? that comes from the for loop, so each output on the for loop (betweeen 1,11) will now be taken and **2
print(squares)



