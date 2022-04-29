"""
Entradas
Primer número (int) -> a
Segundo número (int) -> b

Salidas
Repetición (int)
"""
#Entradas
a=int(input("Ingrese primer número entero: "))
b=int(input("Ingrese segundo número entero: "))
a2=a
b2=b
#Caja negra while
print("Repetición en while: ")
while (a>0):
    a = a - b
    print (a)
#Salida while
print(f"El restante efectuado es: {a}")

#Caja negra for
print("Repetición en for: ")
for a2 in range (a2, 0, -b2):
    a2 = a2 - b2
    print (a2)
print(f"El restante efectuado es: {a2}")