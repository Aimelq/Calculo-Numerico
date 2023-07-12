from math import *
#AIMEL QUIJADA. CI:30.729.553

def algoritmo_biseccion(f, a, b, Es, NI):
    Ea= 100 #este es el error aproximado relativo
    i= 1 #contador de iteraciones
    Pm_actual= a #punto medio actual
    Pm_anterior= b #punto medio anterior
    print('Algoritmo bisección')
    while (i < NI and Ea > Es):
        Pm_anterior = Pm_actual
        Pm_actual = (a + b)/2

        if (f(Pm_actual)*f(b) < 0):
            a = Pm_actual
        else:
            b = Pm_actual
        Ea = abs((Pm_actual - Pm_anterior)/Pm_actual)
        print ('Iteración:',i,' Intervalo: [',a,',',b,']')	
        i = i + 1
	    
    print ('El error relativo es: ',Ea,'')


f = lambda x: e**x - 3*x**2 
a =	0 #intervalo a
b = 1 #intervalo b
Es = 0.03 #la aproximación del error que hay que calcular debe ser menor a 0.03
NI = 75 #máximo de iteraciones
Error = algoritmo_biseccion(f, a, b, Es, NI)