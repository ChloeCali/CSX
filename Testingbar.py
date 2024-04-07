import numpy as np 
import matplotlib.pyplot as plt 
 
# set width of bar 
barWidth = 10
fig = plt.subplots(figsize =(12, 8)) 
 
# set height of bar 
IT = [-30839.0, -3719.0, 1.0, 4321.0]
 
# Set position of bar on X axis 
br1 = [-15.0, -5.0, 5.0, 15.0]

# Make the plot
plt.bar(br1, IT, color ='r', width = barWidth, edgecolor ='grey', label ='IT') 
 
plt.show() 