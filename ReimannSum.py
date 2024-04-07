import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Poly import polynomial

def plotter(polly, x_range):
    x = [i for i in range(x_range[0], x_range[1])]
    y = [polly.plugin(i) for i in x]
    return x,y

def LRS(polly, xlim1, xlim2, sections, distance):
    sect = float(distance/sections)


    cnt1 = 0
    coord = xlim1
    xcoords = []
    heights = []
    while cnt1 < sections:
        xcoords.append(coord)
        coord = coord + sect
        cnt1 = cnt1 + 1

    
    cnt2 = 0
    while cnt2 < sections:
        heights.append(polly.plugin(xcoords[cnt2]))
        cnt2 = cnt2 + 1
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)


    realxcoords = []
    cnt3 = 0
    while cnt3 < sections:
        realxcoords.append(sect/2 + xcoords[cnt3])
        cnt3 = cnt3 + 1

    # Make the plot
    
    cnt4 = 0
    area = 0
    while cnt4 < sections: 
        area = area + (heights[cnt4]*sect)
        cnt4 = cnt4 + 1
    
    area = str(area)
    sect = int(sect)

    far1 = sect + xlim2
    far2 = xlim1 - sect

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.bar(realxcoords, heights, color ='r', width = sect, edgecolor ='grey')
    plt.title("Left Reimann sum = " + area)
    plt.show()

def RRS(polly, xlim1, xlim2, sections, distance):
    sect = float(distance/sections)

    cnt1 = 0
    coord = xlim1
    coord = xlim1 + sect
    xcoords = []
    heights = []
    while cnt1 < sections:
        xcoords.append(coord)
        coord = coord + sect
        cnt1 = cnt1 + 1

    
    cnt2 = 0
    while cnt2 < sections:
        heights.append(polly.plugin(xcoords[cnt2]))
        cnt2 = cnt2 + 1
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)


    realxcoords = []
    cnt3 = 0
    while cnt3 < sections:
        realxcoords.append(sect/2 + xcoords[cnt3]-sect)
        cnt3 = cnt3 + 1

    # Make the plot
    
    cnt4 = 0
    area = 0
    while cnt4 < sections: 
        area = area + (heights[cnt4]*sect)
        cnt4 = cnt4 + 1
    
    area = str(area)
    sect = int(sect)

    far1 = sect + xlim2
    far2 = xlim1 - sect

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.bar(realxcoords, heights, color ='r', width = sect, edgecolor ='grey')
    plt.title("Right Reimann sum = " + area)
    plt.show()

def TRS(polly, xlim1, xlim2, sections, distance):
    sect = float(distance/sections)


    cnt1 = 0
    coord = xlim1
    xcoords = []
    heights = []
    while cnt1 < sections:
        xcoords.append(coord)
        coord = coord + sect
        cnt1 = cnt1 + 1

    
    cnter1 = 0
    cnter2 = 1
    height1 = polly.plugin(xcoords[cnter1])
    height2 = polly.plugin(xcoords[cnter2])
    
    while cnter2 < len(xcoords):
        if height1 < height2:
            heights.append(height1)
            cnter1 = cnter1 + 1
            cnter2 = cnter2 + 1
            height1 = polly.plugin(xcoords[cnter1])
            height2 = polly.plugin(xcoords[cnter2])
        elif height1 > height2:
            heights.append(height2)
            cnter1 = cnter1 + 1
            cnter2 = cnter2 + 1
            height1 = polly.plugin(xcoords[cnter1])
            height2 = polly.plugin(xcoords[cnter2])
        else: 
            heights.append(height1)
            cnter1 = cnter1 + 1
            cnter2 = cnter2 + 1
            height1 = polly.plugin(xcoords[cnter1])
            height2 = polly.plugin(xcoords[cnter2])
            
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)


    realxcoords = []
    cnt3 = 0
    while cnt3 < sections:
        realxcoords.append(sect/2 + xcoords[cnt3])
        cnt3 = cnt3 + 1

    # Make the plot
    
    cnt4 = 0
    area = 0
    while cnt4 < sections: 
        area = area + (heights[cnt4]*sect)
        cnt4 = cnt4 + 1
    
    area = str(area)
    sect = int(sect)

    far1 = sect + xlim2
    far2 = xlim1 - sect

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.bar(realxcoords, heights, color ='r', width = sect, edgecolor ='grey')
    plt.title("Left Reimann sum = " + area)
    plt.show() 

    #right triangle
    plt.plot(-1, -7, marker = 'o', color = 'red')
    plt.plot(4, -7, marker = 'o', color = 'purple')
    plt.plot(-1, -1, marker = 'o', color = 'green')

    plt.plot(
        [-1, 4, -1, -1],
        [-7, -7, -1, -7]
    )
    plt.fill(
        [-1, 4, -1, -1],
        [-7, -7, -1, -7],
        color = '#d733ff'
    )

    #right angle marker
    plt.plot(
        [-1, -0.5, -0.5],
        [-6, -6, -7],
        color = 'black'
    ) 


def main():
    array = []
    
    degree = int(input("coefficients: "))

    cnt = 0

    while cnt < degree:
        adder = int(input("insert: "))
        array.append(adder)
        cnt = cnt + 1

    polly = polynomial(array)

    xlim1 = float(input("x limit 1 = "))
    xlim2 = float(input("x limit 2 = "))
    sections = float(input("sections = "))
    distance = float(abs(xlim1) + abs(xlim2))

    LRS(polly, xlim1, xlim2, sections, distance)
    RRS(polly, xlim1, xlim2, sections, distance)


if __name__ == "__main__":
    main()





