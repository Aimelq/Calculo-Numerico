from math import *
#AIMEL QUIJADA. CI:30.729.553


def algoritmo_Newton_Raphson(f, dev_f, Ni, a, b, Es):
    Ea= 100 
    i= 0
    xi = (a + b)/2 #el punto medio entre el intervalo [a, b]
    
    while(i < Ni and Ea > Es):
        xi_1 = xi - (f(xi)/dev_f(xi))
        print('Iteración: ',i,' | Xi: ',xi,' | Xi + 1:',xi_1,'')
        Ea = abs((xi_1 - xi)/ xi_1) #para calcular el error relativo
        xi = xi_1
        i = i + 1
        
    print('El error relativo es:',Ea,'')
           
print('Algoritmo Newton-Raphson')           
f = lambda x: e**x - 3*x**2  # esta es la función e^x-3x^2
dev_f = lambda x: e**x-6*x #esta es la derivada de la función. e^x-6x
Es = 0.02 #las iteraciones paran cuando el error relativo sea menor a 0.02
Ni = 25 #máximo de iteraciones
a = 0 #intervalo a
b = 1 #intervalo b
Error = algoritmo_Newton_Raphson(f, dev_f, Ni, a, b, Es)