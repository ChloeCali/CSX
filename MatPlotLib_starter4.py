import matplotlib.pyplot as plt

import matplotlib.animation as animation

import numpy as np



# Set up figure and axes

fig, ax = plt.subplots()

ax.set_aspect('equal')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)




# Initialize Earth a

earth_x = 20

earth_y = 0

moon_x = 1

moon_y = 0



# Create Earth and Moon objects

earth = plt.Circle((earth_x, earth_y), 1, fc='blue')

moon = plt.Circle((moon_x, moon_y), .5, fc='gray')



# Add Earth and Moon to axes

ax.add_patch(earth)

ax.add_patch(moon)



# Define animation function

def animate(i):

# Update Moon position

  moon_x = 0.5 * np.cos(i * .5)

  moon_y = 0.5 * np.sin(i * .5)

  moon.center = (moon_x, moon_y)

  # Update Earth position

  earth_x = np.cos(i * 20)

  earth_y = np.sin(i * 0.005)

  earth.center = (earth_x, earth_y)

  return earth, moon



# Create animation

ani = animation.FuncAnimation(fig, animate, frames=2000, blit=True, interval=20)



# Show plot

plt.show()