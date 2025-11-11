print('\n') 

from pathlib import Path
import csv 
from datetime import datetime 

import matplotlib.pyplot as plt

# =================== Importing and Plottings data over a small timeframe 


# path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# lines = path.read_text().splitlines() #this helps us read the file, and then get the list of all lines in the files. 

# reader = csv.reader(lines) #this can parse each line into a file. 
# header_row = next(reader) #when we give it the reader object this returns the next line starting at the beginning 

# # print(header_row)

# #Printing headers and their positions 
# # for index, column_header in enumerate(header_row):
# #     print(index, column_header)


# # # Extract high temps 
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d') #this will grab the date data from the csv and convert it into the format we want it to be shown
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# # print(highs)

# # Plot the high temps 
# plt.style.use("seaborn-v0_8")
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format the plot. 
# ax.set_title("Daily High Temps, July 2021", fontsize=24)
# ax.set_xlabel("", fontsize=16)
# fig.autofmt_xdate() # this draws the dates diagonally to prevent overlap in appearing text
# ax.set_ylabel("Temps (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

# print('\n') 

# =================== Importing and Plottings data over a longer timeframe 


path = Path('weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines() #this helps us read the file, and then get the list of all lines in the files. 

reader = csv.reader(lines) #this can parse each line into a file. 
header_row = next(reader) #when we give it the reader object this returns the next line starting at the beginning 

# print(header_row)

#Printing headers and their positions 
# for index, column_header in enumerate(header_row):
#     print(index, column_header)


# # Extract high temps 
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d') #this will grab the date data from the csv and convert it into the format we want it to be shown
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# print(highs)

# Plot the high temps 
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format the plot. 
ax.set_title("Daily High Temps, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate() # this draws the dates diagonally to prevent overlap in appearing text
ax.set_ylabel("Temps (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

print('\n') 