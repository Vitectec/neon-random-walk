# Import the pyplot module from the matplotlib library under the alias plt for plotting graphs
import matplotlib.pyplot as plt

# Import the choice function from the built-in random module.
# The choice() function takes a list and returns one random element from it.
from random import choice

# Create the x_values list and immediately add the first X coordinate, 0 (the starting point)
x_values = [0]

# Create the y_values list and immediately add the first Y coordinate, 0 (the starting point)
y_values = [0]

# Start a while loop.
# The len() function counts the current length of the list. The loop will run until there are 5000 elements in the list.
while len(x_values) < 5000:
    # Calculate the step along the X-axis: the choice() function randomly selects a direction (-1 or 1)
    # and multiplies it by a randomly selected distance (a number from 1 to 4) from the second list.
    x_step = choice([-1, 1]) * choice([1, 2, 3, 4])

    # Calculate the step along the Y-axis: similarly select a random direction and step length vertically.
    y_step = choice([-1, 1]) * choice([1, 2, 3, 4])

    # Calculate the next X coordinate: take the last element from the x_values list.
    # The [-1] index in Python always means "the very last element in the list". Add x_step to it.
    next_x = x_values[-1] + x_step

    # Calculate the next Y coordinate: take the very last element from the y_values list and add y_step to it.
    next_y = y_values[-1] + y_step

    # The .append() method adds the calculated value (next_x) to the very end of the x_values list.
    x_values.append(next_x)

    # The .append() method adds the calculated value (next_y) to the very end of the y_values list.
    y_values.append(next_y)

# The subplots() function creates a window for the plot (fig) and the drawing area itself (ax).
# The figsize=(10, 6) parameter sets the size of this area: 10 inches wide and 6 inches high.
fig, ax = plt.subplots(figsize=(10, 6))

# The ax.plot() method sequentially connects all points from the x_values and y_values lists with a solid line.
# linewidth=1 sets the line thickness, color='#00F5FF' sets a neon color, and alpha=0.8 makes the line slightly transparent.
ax.plot(x_values, y_values, linewidth=1, color='#00F5FF', alpha=0.8)

# The ax.scatter() method draws individual points on the plot. Here we draw ONE point at coordinates (0,0).
# c="green" makes it green, s=100 sets a large size, and edgecolors="none" removes the black outline around the point. This is the Start.
ax.scatter(0, 0, c="green", s=100, edgecolors="none")

# Call ax.scatter() again to draw ONE final point.
# Coordinates are taken from the end of the lists using the [-1] index. c="red" makes it red. This is the Finish.
ax.scatter(x_values[-1], y_values[-1], c="red", s=100, edgecolors="none")

# The ax.get_xaxis() method gets the horizontal axis, and .set_visible(False) completely hides it (numbers and ticks).
ax.get_xaxis().set_visible(False)

# The ax.get_yaxis() method gets the vertical axis, and .set_visible(False) hides it for a clean design.
ax.get_yaxis().set_visible(False)

# The plt.title() function adds the text title "Random Walk Visualization" to the very top of the window.
plt.title("Random Walk Visualization")

# The plt.show() function takes everything we drew using the ax object methods, opens a graphical window, and displays it on the screen.
plt.show()

