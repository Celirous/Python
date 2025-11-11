print('\n') 

from random import choice

class RandomWalk: 
    """A class to enerate rnadom walks"""


    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walk start at (0, 0). 
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking stesp until the walk reaches the desured length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go,, and how far to go
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance 

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject move that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# CHATGPT Summary

# Purpose: Defines the RandomWalk class, which creates a series of random steps.
# Key points:
# Uses random.choice() to determine both direction (+ or -) and distance (0–4 units) for each step.
# Starts every walk at the origin (0, 0) and continues until it reaches the specified number of points (num_points, default 5000).
# Ensures that no step results in no movement (both x and y = 0).
# Stores all x and y coordinates in self.x_values and self.y_values.