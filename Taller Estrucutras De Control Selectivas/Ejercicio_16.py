"""
Entradas
a (float)
b (float)
c (float)

Salidas
Valor de x1 (float) -> x1
Valor de x2 (float) -> x2
"""
#Entradas
from cmath import sqrt


a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))
c = float(input("Ingresar el valor de c: "))

#Caja negra
d = ((b**2 )-(4*(a*c)))

x1=""
x2="" 

if (d == 0):
    x2 = (-b(2*a))
    x1 = x2
elif (d > 0):
    x1 = (-b + sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*(a*c))))/(2*a)
elif (d < 0):
    x1 = "No tiene solución en los reales"
    x2 = "No tiene solución en los reales"

#Salidas
print (f"El valor de x1 es: {x1}")
print (f"El valor de x2 es: {x2}")