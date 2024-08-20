#import matplotlib.pyplot as plt
#import numpy as np

#def f(t):
#    return 0.4*t

#def g(t):
#    return 0.3*t

#x = np.arange(0, 6, 0.01) # genera una lista

#y1 = f(x)
#y2 = g(x)

#plt.plot(x, y1) # coloca las listas en puntos en el plano
#plt.plot(x, y2) # coloca las listas en puntos en el plano

#plt.xlabel("Eje x") # Titulo para el eje x
#plt.ylabel("Eje y") # Titulo para el eje y
#plt.title("Prueba del concepto") # Titulo para el grafico

#plt.grid(True) # Ingresa la cuadricula

#plt.show()

import matplotlib.pyplot as mt
import numpy

def generar_eje_x(cantidad):
    x = numpy.arange(0, cantidad, 0.01)
    return x

# Distancia recorrida

def f(t):
    return 0.4*t

def g(t):
    return 0.3*t

# |---------------------|

x = generar_eje_x(180)

yf = f(x)
yg = g(x)

mt.plot(x, yf)
mt.plot(x, yg)

mt.grid(True)

mt.show()