print('\n')

#for loops in Python

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())
# this is a normal for loop. It will output each name in the list (array) of magicians info 
print('\n') 

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
# this will output a sentance with each name in the list on it
print('\n')


for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'\tI cannot wait to see the next trick, {magician.title()}\n')
# this now outputs 2 sentances per loop it is making through the list 
print('\n')

for magician in magicians:
    print(f'{magician.title()}, that was an awesome trick!')
    print(f'\tI cannot wait to see the next one, {magician.title()}\n')

print(f'Thank you everyone, that was the whole magic show!')
# this is now outputting 2 sentances per loop and then when it is done, it outputs one more thing. 
print('\n')


# running the for loop without making the indeting and getting an error |
                                                                   #    v 
# for magician in magicians:
# print(f'{magician.title()}, that was an awesome trick!') #this is the error in question, it wants you to indent (tab space), so that it indicates within it that this is part of the for loop 

#running the for loop with the indent in the wrong place  |
#                                                         v
# for magician in magicians:
#     print(f'{magician.title()}, that was an awesome trick!')
# print(f'\tI cannot wait to see the next one, {magician.title()}\n') #so this will run the loop but the second print will only output at the end of the loop. 
 

#indentin unnecessarily can make it output in side the loop and not as the last output. |
#                                                                                       v
# for magician in magicians:
#     print(f'{magician.title()}, that was an awesome trick!')
#     print(f'\tI cannot wait to see the next one, {magician.title()}\n')

#     print(f'Thank you everyone, that was the whole magic show!')

#this will make it so that it output each time in the loop and not outside


# you can also forget the ":" after the for loop and it will break 

# for magician in magicians                 # <-- no colon added there, issue
#     print(f'{magician.title()}, that was an awesome trick!')
#     print(f'\tI cannot wait to see the next one, {magician.title()}\n')

# print(f'Thank you everyone, that was the whole magic show!')

print('\n')



