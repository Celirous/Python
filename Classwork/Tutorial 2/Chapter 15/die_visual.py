print('\n') 

import plotly.express as px
from d_die import Die

# Create two D6's
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list 
results = []

for roll_num in range(1000): #the range(100) means how many times it is going to do this 
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyze the results
frequencies = [] #this is checking how frequently something appears
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_results+1) # we are basically counting how many times a number will appear

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualise the results
title = "Results of rolling two D6, 1000 times"
labels = {"x": 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize the chart.
fig.update_layout(xaxis_dtick=1)

fig.show()


# print(results)

# print('\n')

# print(frequencies)

# print('\n') 
