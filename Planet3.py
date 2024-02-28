
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

earth_x = []
earth_y = []

Vx = 0
Vy = 8000
x = (4.00 *(10**(-11)))
y = 0
G = (6.67 *(10**(-11)))
M = (5.00 *(10**24)) 
delta = 5

fig, ax = plt.subplots()

earth_path = ax.plot(0, 0)

sun = plt.Circle((2.5*(10**6), 2.5*(10**6)), 10000, fc='yellow')

ax.add_patch(sun)

def orbit(d): 
  
    Vx = (Ax*delta) + Vx
    Vy = (Ay*delta) + Vy
    Ax = -1*G*M*x((x**2)+(y**2))**(1.5)
    Ay = -1*G*M*y((x**2)+(y**2))**(1.5)

    if len(earth_x) == 0 and len(earth_y) == 0:
        earth_x.append(x)
        earth_y.append(y)

    else:
        earth_x.append(earth_x[len(earth_x) - 1] + Vx * delta)
        earth_y.append(earth_y[len(earth_y) - 1] + Vy * delta)

    earth_path.set_xdata(earth_x)
    earth_path.set_ydata(earth_y)

  
    return earth_path

animation = FuncAnimation(fig, func=orbit, frames= 360, interval=25)

plt.xlim([-2,5*(10**6)])
plt.ylim([-2, 5*(10**6)])

plt.xticks([])
plt.yticks([])

plt.show()