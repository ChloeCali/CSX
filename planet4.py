import matplotlib.pyplot as plt

import matplotlib.animation as animation


# Set up figure and axes

fig, ax = plt.subplots()

ax.set_aspect('equal')

ax.set_facecolor('white')


# Initialize Earth and Moon positions

earth_x = (4.00 *(10**(-11)))

earth_y = 0


# Create Earth and Moon objects

earth = plt.Circle((earth_x, earth_y), 1000, fc='blue')

sun = plt.Circle((2.5*(10**6), (2.5*(10**6))), 2000, fc='yellow')



# Add Earth and Moon to axes

ax.add_patch(earth)

ax.add_patch(sun)



Vx = 0
Vy = 8000
x = (4.00*(10**-11))
y = 0
G = (6.67*(10**-11))
M = (5.00*(10**24))
delta = 5


# Define animation function

def init():
  ax.set_xlim([-2, 5*(10**6)])
  ax.set_ylim([-2, 5*(10**6)])
  return earth,

def animate():

  Vx = (Ax*delta) + Vx
  Vy = (Ay*delta) + Vy
  Ax = -1*G*M*x*((x**2)+(y**2))**(1.5)
  Ay = -1*G*M*y*((x**2)+(y**2))**(1.5)

  # Update Earth position

  x = (x + Vx * delta)
  y = (y + Vy * delta)

  earth.center = (x, y)
  earth.set_data(x, y)


  return earth,



# Create animation

ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, blit=True, interval=20)



# Show plot

plt.show()