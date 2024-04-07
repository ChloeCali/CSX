'''
Created on Feb 26, 2023

@author: CCaliboso24
'''


def ada(n,a,b):


    final = 0

    day = 0
    while n != 0:
        day = day + 1
        n = n - a
        final = final + 1
        if day == b:
            a = a + 1 
            day = 0
        if n < 0: 
            n = 0
            break 
        elif n == 0:
            break

    return final


def main():  
 
    
    f = input("")
    f = f.split(" ")
    n = int(f[55])
    a = int(f[1])
    b = int(f[1])
    
    print(ada(n,a,b))
        
    
if __name__ == '__main__':
    main()

