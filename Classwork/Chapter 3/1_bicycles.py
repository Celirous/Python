#we are doing lists, like with JS they are arrays, with Py it is a 
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
#accessing info inside the list
print(f"First element in the List: {bicycles[0].title()}") #the .title makes the first thing a capital letter for you
print('\n')

print(f"Third element in the List: {bicycles[2].title()}") 
print(f"Last element in the List: {bicycles[-1].title()}") #the '-' means it is counting from the back of it. So this will be the last on in the list 

print('\n')

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
