import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math




# Define the figure and axis
fig, ax = plt.subplots()

Vx = 0
Vy = 8000
x = (4.00 *(10**-11))
y = 0

# Define the animation function
def animate(i):
# Clear the axis for each iteration
    ax.clear()

    delta = 5
    G = (6.67 *(10**-11))
    M = (5.00 *(10**24)) 
    Vx = (Ax*delta) + Vx
    Vy = (Ay*delta) + Vy
    Ax = -1*G*M*x((x**2)+(y**2))**(1.5)
    Ay = -1*G*M*y((x**2)+(y**2))**(1.5)

    # Define the angle
    angle = i/100

    # Calculate the x and y coordinates for the ellipse
    x = x + Vx * delta
    y = y + Vy * delta

    # Plot the ellipse
    ax.plot(x, y, 'ro')

    # Set the axis limits
    ax.set_xlim((-3*(10**6)), (5*(10**6)))
    ax.set_ylim((-4*(10**6)), (4*(10**6)))


ani = animation.FuncAnimation(fig, animate, frames=360, interval=5)
plt.show()

