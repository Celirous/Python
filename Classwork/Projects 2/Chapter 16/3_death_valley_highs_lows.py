print('\n') 

from pathlib import Path
import csv 
from datetime import datetime 

import matplotlib.pyplot as plt


# =================== Importing and Plottings data over a large timeframe 
# =================== Plotting a second data series

path = Path('weather_data/death_valley_2021_simple.csv')

lines = path.read_text().splitlines() #this helps us read the file, and then get the list of all lines in the files. 

reader = csv.reader(lines) #this can parse each line into a file. 
header_row = next(reader) #when we give it the reader object this returns the next line starting at the beginning 

# print(header_row)

#Printing headers and their positions 
# for index, column_header in enumerate(header_row):
#     print(index, column_header)


# # Extract high temps, dates and the low temps
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d') #this will grab the date data from the csv and convert it into the format we want it to be shown
    try:
        high = int(row[3]) #this is grabbing info in row 3 and assisgning all the info to the high var
        low = int(row[4]) # this is grabbing info in row 4 and assigning all the info to the low var 
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# print(highs)

# Plot the high temps and the low temps
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots() #this actually makes the graph
ax.plot(dates, highs, color='red', alpha=0.5) #this prints out the highs 
ax.plot(dates, lows, color='blue', alpha=0.5)# this prints out the lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #this is the filling between the two results 

# Format the plot. 
title = f"Daily high and low temps, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate() # this draws the dates diagonally to prevent overlap in appearing text
ax.set_ylabel("Temps (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

print('\n') 

#================== AI Summary 
# Chat GPT Summary
# It imports necessary libraries:
# pathlib to locate and read the CSV file.
# csv to process the file’s data.
# matplotlib.pyplot to create the graph.
# datetime to convert date strings into date objects.
# The program opens the CSV file containing weather data for Death Valley.
# It reads the header row to identify which columns contain the date, high, and low temperatures.
# It then loops through the remaining rows, converting the date strings into Python datetime objects and storing the high and low temperatures in separate lists.
# If any data is missing, it prints a warning message showing which date has missing information.
# Using Matplotlib, it plots the daily high temperatures in red and low temperatures in blue.
# It shades the area between the high and low lines to visually highlight the temperature range.
# The chart includes a title, axis labels, and formatted dates for readability.
# Finally, it displays the graph, showing how temperatures varied throughout the year in Death Valley.