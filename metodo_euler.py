from math import *
#Aimel Quijada. C.I: 30.729.553

def metodo_euler(f, t0, y0, tn, n):
    h = (tn - t0) / n
    t = t0
    y = y0
    
    for i in range(n +1):
        y_1 = y + h * f(t, y)
        print('i: ', i, '| Ti: ', t, '| Yi: ', y, '| Y+1:', y_1)
        t = t + h
        y= y_1
        
    return y

def f(t, y):
    return (t - y) ** 2 + 1

print ('Método Euler')
t0 = 2
y0 = 1
tn = 3
n = 4

metodo_euler(f, t0, y0, tn, n)