

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the ellipse parameters
a = 5
b = 3
x0 = 0
y0 = 0

# Define the animation function
def animate(i):
# Clear the axis for each iteration
    ax.clear()

    # Define the angle
    angle = i/25

    # Calculate the x and y coordinates for the ellipse
    x = x0 + a * np.sin(angle)
    y = y0 + b * np.sin(angle)

    # Plot the ellipse
    ax.plot(x, y, 'ro')

    # Set the axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

# Call the animation function and display the animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=5)
plt.show()