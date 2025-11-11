print('\n') 

import matplotlib.pyplot as plt

from c_random_walk import RandomWalk


#======================== Making a random walk

 
# rw = RandomWalk()
# rw.fill_walk()

# # Make a random walk.
# # Plot the points in the walk. 
# plt.style.use("classic")
# fig, ax = plt.subplots()

# ax.scatter(rw.x_values, rw.y_values,y s=15)
# ax.set_aspect("equal")

# plt.show()


#====================== Making mutiple new walks, as long as the program is active 


while True:
    # Make a random walk. 
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors="none", s=1)
    ax.set_aspect("equal")

    # Emphasize the first and last points
    ax.scatter(0, 0, c='red', edgecolors="none", s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors="none", s=50)

    # Remove the axes. 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


# ChatGPT summary

# Purpose: Handles visualization and user interaction for random walks.
# Key points:
# Continuously generates new random walks while the program runs.
# Plots up to 50,000 points per walk using Matplotlib with the "classic" style.
# Colors points using a green gradient (cmap=plt.cm.Greens) to show progression through the walk.
# Highlights:
# Starting point in red.
# Ending point in blue.
# Removes axes for a cleaner visualization.
# Prompts the user (input("Make another walk? (y/n)")) to continue or quit after each walk.