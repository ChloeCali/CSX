import numpy as np

def function(x):
    return .173 * x + 6.87

psi = 120
angle = np.radians(45)

vel = function(psi)

time = np.sin(angle) * function(psi) / 4.9

range = np.cos(angle) * vel * time

print(time)
print(range)
print(vel)