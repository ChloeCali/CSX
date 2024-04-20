'''
Created on Feb 26, 2023

@author: CCaliboso24
'''
import numpy as np
import matplotlib.pyplot as plt
from Poly import polynomial
import matplotlib.patches as patches
from sympy import symbols, integrate

def calcular_integral(function, variable, xlim1, xlim2):
    
    x = symbols(variable)
    integral = integrate(function, (x, xlim1, xlim2))
    return integral



def main():  

    # Solicitar la función y los límites al usuario
    function = input("Ingrese la función: ")
    variable = input("Ingrese la variable de integración: ")
    limite_inferior = float(input("Ingrese el límite inferior: "))
    limite_superior = float(input("Ingrese el límite superior: "))

    # Calcular la integral definida
    resultado = calcular_integral(function, variable, limite_inferior, limite_superior)
    print("Resultado:", resultado)
 

if __name__ == '__main__':
    main()
