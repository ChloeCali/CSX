import numpy as np
import matplotlib.pyplot as plt
from Poly import polynomial
import matplotlib.patches as patches


def plotter(polly, x_range):                            #plots function
    x = [i for i in range(x_range[0], x_range[1])]
    y = [polly.plugin(i) for i in x]
    return x,y

def LRS(polly, xlim1, xlim2, sections, distance): 
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)
    sect = float(distance/sections)                     #length of each subdivision



    cnt = 0
    coord = xlim1
    xcoords = []
    heights = []
    while cnt < sections:                               #loop creates an array of the x coordinates of every subdivision
        xcoords.append(coord)
        coord = coord + sect
        cnt = cnt + 1

    
    cnt = 0
    while cnt < sections:                               #loop plugs in each x coordinate to create an array of y coordinates
        heights.append(polly.plugin(xcoords[cnt]))
        cnt = cnt + 1


    realxcoords = []                                    #loop finds real x coordinates for the bars so they arent aligned at the midpoint
    cnt = 0
    while cnt < sections:                               
        realxcoords.append(sect/2 + xcoords[cnt])
        cnt = cnt + 1

    # Make the plot
    
    cnt = 0
    area = 0
    while cnt < sections:                               #loop calculates accumulated area of the bars
        area = area + (heights[cnt]*sect)
        cnt = cnt + 1
    
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
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)
    sect = float(distance/sections)                     #length of each subdivision

    cnt = 0
    coord = xlim1
    coord = xlim1 + sect
    xcoords = []
    heights = []
    while cnt < sections:                               #loop creates an array of the x coordinates of every subdivision
        xcoords.append(coord)
        coord = coord + sect
        cnt = cnt + 1

    
    cnt = 0
    while cnt < sections:                               #loop plugs in each x coordinate to create an array of y coordinates
        heights.append(polly.plugin(xcoords[cnt]))
        cnt = cnt + 1
    

    realxcoords = []
    cnt = 0
    while cnt < sections:
        realxcoords.append(sect/2 + xcoords[cnt]-sect) #loop finds real x coordinates for the bars so they arent aligned at the midpoint
        cnt = cnt + 1

    # Make the plot
    
    cnt = 0
    area = 0
    while cnt < sections:                               #loop calculates accumulated area of the bars
        area = area + (heights[cnt]*sect)
        cnt = cnt + 1
    
    area = str(area)
    sect = int(sect)

    far1 = sect + xlim2
    far2 = xlim1 - sect

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.bar(realxcoords, heights, color ='r', width = sect, edgecolor ='grey')
    plt.title("Right Reimann sum = " + area)
    plt.show()

def MRS(polly, xlim1, xlim2, sections, distance):
     
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)
    sect = float(distance/sections)


    cnt = 0
    coord = xlim1
    xcoords = []
    heights = []
    
    while cnt < sections:
        xcoords.append(coord)
        coord = coord + sect
        cnt = cnt + 1

    
    cnt = 0
    while cnt < sections:
        heights.append(polly.plugin(xcoords[cnt] + (sect/2)))
        cnt = cnt + 1

    realxcoords = []
    cnt = 0
    while cnt < sections:
        realxcoords.append(sect/2 + xcoords[cnt])
        cnt = cnt + 1

    # Make the plot
    
    cnt = 0
    area = 0
    while cnt < sections: 
        area = area + (heights[cnt]*sect)
        cnt = cnt + 1
    
    area = str(area)
    sect = int(sect)

    far1 = sect + xlim2
    far2 = xlim1 - sect

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.bar(realxcoords, heights, color ='r', width = sect, edgecolor ='grey')
    plt.title("Midpoint Reimann sum = " + area)
    plt.show()

def TRS(polly, xlim1, xlim2, sections, distance):
    
    xlim1 = int(xlim1)
    xlim2 = int(xlim2)
    sect = float(distance/sections)


    cnt = 0
    coord = xlim1
    xcoords = []
    heights = []
    while cnt <= sections:
        xcoords.append(coord)
        coord = coord + sect
        cnt = cnt + 1

    cnt1 = 0
    cnt2 = 1

    #y
    while cnt2 <= sections:
        two = int(polly.plugin(xcoords[cnt1]))
        three = int((polly.plugin(xcoords[cnt2])))
        heights.append([0,two,three,0])
        cnt1 = cnt1 + 1
        cnt2 = cnt2 + 1
    

    cnt1 = 0
    cnt2 = 1
    realxcoords = []
    #x
    while cnt2 <= sections:
        one = int(xcoords[cnt1])
        two = int(xcoords[cnt2])
        realxcoords.append([one,one,two,two])
        cnt1 = cnt1 + 1
        cnt2 = cnt2 + 1


    far1 = int(sect + xlim2)
    far2 = int(xlim1 - sect)

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='auto')
    ax.set_xlim(xlim1, xlim2)

    cnt = 0
    while cnt < sections:
        ax.add_patch(patches.Polygon(xy=list(zip(realxcoords[cnt],heights[cnt])), fill=False))
        cnt = cnt + 1


    area = 0
    cnt = 0
    while cnt < sections:
        ytrap = heights[cnt]

        a = int(ytrap[1])
        b = int(ytrap[2])
        h = int(sect)

        area = area + (((a+b)/2)*h)
        cnt = cnt + 1
    
    area = str(area)

    x,y = plotter(polly, [far2,far1])
    plt.plot(x,y)
    plt.title("Trapezoid Reimann sum = " + area)
    plt.show() 

def main():


    array = []

    degree = int(input("degree: "))

    cnt = 0
    while cnt <= degree:
        coeff = int(input("insert coefficient: "))
        array.append(coeff)
        cnt = cnt + 1
    

    polly = polynomial(array)

    xlim1 = int(input("lower x limit:"))
    xlim2 = int(input("upper x limit:"))
    sections = int(input("sections: "))
    distance = float(abs(xlim1) + abs(xlim2))

    func = input("choose LRS, RRS, MRS, TRS: ")
    if func == "LRS":
        LRS(polly, xlim1, xlim2, sections, distance)
    elif func == "RRS": 
        RRS(polly, xlim1, xlim2, sections, distance)
    elif func == "MRS":
        MRS(polly, xlim1, xlim2, sections, distance)
    elif func == "TRS":
        TRS(polly, xlim1, xlim2, sections, distance)
    else:
        print("invalid")
    

if __name__ == "__main__":
    main()