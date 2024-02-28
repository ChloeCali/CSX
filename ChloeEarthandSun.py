import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#givens
Vxi = [0.00]
Vyi = [8000.00]
x = 4000000.00
y = 80000.00
G = 0.0000000000667
M = 5e24
delta = 10

#holder arrays for animation function
holderx = []
holdery = []

holderpathx = []
holderpathy = []

holdersunx = []
holdersuny = []

#creating plot
fig, ax = plt.subplots()

#plotting sun and earth and earth's path
xdata, ydata = [x], [y]
sunxdata, sunydata = [-3627.841404], [31075.425]

earthpath, = ax.plot(0, 0, 'b')
earth, = ax.plot(0, 0,'bo')
sun, = ax.plot(0,0, 'yo')


#creating arrays that hold x and y values of earth's orbital path
counter = 0
while counter < 800:

  xuse = xdata[len(xdata) -1]
  yuse = ydata[len(ydata) -1]
  Ax = -1*G*M*xuse*((xuse**2) +(yuse**2))**(-1.5)
  Ay = -1*G*M*yuse*((xuse*xuse)+(yuse*yuse))**(-1.5)

  if counter == 0:
    Vx = Vxi[0]
    Vy = Vyi[0]
    counter = counter + 1
  else: 
    Vx = (Ax*delta) + Vxi[len(Vxi) -1]
    Vy = (Ay*delta) + Vyi[len(Vyi) -1]
    Vxi.append(Vx)
    Vyi.append(Vy)

    x = (xuse + Vx * delta)
    y = (yuse + Vy * delta)

    xdata.append(x)
    ydata.append(y)

    counter = counter + 1


#creating arrays that hold x and y values of sun
counter = 0
while counter < 1000:
  sunxdata.append(-3627.841404)
  sunydata.append(31075.425)
  counter = counter + 1

#initial function setting axis limits
def init():
  ax.set_xlim([-3e6, 5e6])
  ax.set_ylim([-4e6, 5e6])
  return earth, earthpath, sun,

#animating function
def animate(i):
  #earth
  holderx.append(xdata[i])
  holdery.append(ydata[i])
  if len(holderx) > 1:
    holderx.pop(0)
    holdery.pop(0)
  earth.set_data(holderx,holdery)

  #earthpath
  holderpathx.append(xdata[i])
  holderpathy.append(ydata[i])
  earthpath.set_data(holderpathx, holderpathy)

  #sun
  holdersunx.append(sunxdata[i])
  holdersuny.append(sunydata[i])
  sun.set_data(holdersunx, holdersuny)

  return earth, earthpath, sun,

ani = animation.FuncAnimation(fig, animate, frames=800, init_func=init, blit=True, interval = 10)


plt.show()