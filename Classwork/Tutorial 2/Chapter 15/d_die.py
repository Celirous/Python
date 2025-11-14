print('\n') 

from random import randint

class Die:
    """A class representing a single die. """

    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)
    

# Chat GPT Summary

# This program simulates rolling two dice — one six-sided and one ten-sided — fifty thousand times. Each time, it adds the results of the two dice and records the total.
# After all the rolls are completed, the program counts how often each possible total appears. For example, some totals like 7 or 8 might appear more frequently than others because there are more combinations that produce those numbers.
# Once all the results are analyzed, the program uses Plotly Express to create a bar chart showing how often each total occurred. The x-axis represents the possible dice totals (from 2 to 16), and the y-axis shows how many times each total appeared.
# Finally, it saves this interactive chart as an HTML file, which can be opened in a web browser to explore the results visually.
# In short, the program demonstrates how random outcomes from dice rolls form a distribution pattern, with some results being more likely than others.
# Chat GPT Summary
# The program simulates rolling two dice: one with 6 sides and another with 10 sides.
# It rolls both dice 50,000 times to collect a large sample of results.
# For each roll, it adds the two dice values together and stores the total.
# After all rolls, it counts how many times each possible total (from 2 to 16) appears.
# It then creates a bar chart using Plotly Express to show the frequency of each total.
# The x-axis of the chart shows the possible dice totals, and the y-axis shows how often each total occurred.
# The chart visually demonstrates that some totals are more common because there are more combinations that can produce them.
# Finally, the chart is saved as an HTML file, which can be opened in a browser for interactive viewing.