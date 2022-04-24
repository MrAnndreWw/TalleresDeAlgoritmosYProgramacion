from cmath import sqrt
import math
"""
Entradas
a (int)
b (int)
c (int)
d (int)

Salidas
Operación (float) -> op
"""
#Entradas
a = int(input("Ingresar valor de a: "))
b = int(input("Ingresar valor de b: "))
c = int(input("Ingresar valor de c: "))
d = int(input("Ingresar valor de d: "))

#Caja negra
op=""

if (d == 0):
    op = ((a-c)**2)
elif (d > 0):
    op = (((a-b)**3)/d)

#Salidas
print(f"El resultado es: {op}")