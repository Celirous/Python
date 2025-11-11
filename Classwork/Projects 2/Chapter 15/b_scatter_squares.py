print('\n') 

import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use("seaborn-v0_8-darkgrid")
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10) # the s= here is the size of the dots on the grid 

# # Set chart title and label axes. 
# ax.set_title("Square Numbers", fontsize=18)
# ax.set_xlabel("Value", fontsize=12)
# ax.set_ylabel("Square of Value", fontsize=12)

# # Set the range for each axis.
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style='plain')

# # Set size of tick labels.
# # ax.tick_params(labelsize=8)

# plt.show()

# ==================== 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10) # the s= here is the size of the dots on the grid #the cmap and c= here is to give us a gradiant starting
                                                                                                                    #with the lowest red value to the darkest red value

# Set chart title and label axes. 
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

# Set size of tick labels.
# ax.tick_params(labelsize=8)

plt.show() #this shows you the actual grid 
plt.savefig('squares_plot.png', bbox_inches='tight') #this will save the data into a picture instead of showing it to us 