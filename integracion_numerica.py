from math import*
#Aimel Quijada
#C.I: 30.729.553

#########################

def suma_riemann(f, a, b, n):
	print('Suma de Riemann')
	h= (b-a)/n
	Acum= 0
	for i in range (n + 1):
		x = a + i * h
		Acum = Acum + h * f(x)
	return Acum
	
#########################	
	
def metodo_trapecio(f, a, b, n):	
	print('Método del trapecio')
	h = (b-a)/n
	acum = 0
	for i in range (n):
		x = a + i * h
		aux = x + h
		acum = acum + ((f(x) + f(aux)) * h)/ 2		
	return acum
			
#########################	

print('Integración numérica')
f = lambda x: (x+1)**0.5 #Aquí está definida la función √(x+1)
X0 = -1 #estos son
Xn= 1 #los intervalos
n= 5
resultado = suma_riemann(f, X0, Xn, n)
print('El resultado es:', resultado)
resultado = metodo_trapecio(f, X0, Xn, n)
print('El resultado es:', resultado)