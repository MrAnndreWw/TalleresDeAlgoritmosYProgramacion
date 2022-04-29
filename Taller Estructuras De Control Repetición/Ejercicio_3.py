"""
Entradas
c (int) -> c

Salidas
Repetición 
"""
#Caja negra while
print("Repetición en while: ")
suma = 0
c = 97
while (c<=1003):
    if(c%2 == 0):
        print(c)
        suma = suma + c
    c = c+1
print (f"La suma total de los números pares comprendidos entre 97 y 1003 es: {suma}")

#Caja negra for
print("Repetición en for: ")
suma2=0
for c2 in range (97, 1004 ,1):
    if (c2%2 == 0):
        print(c2)
        suma2 = suma2 + c2
print (f"La suma total de los números pares comprendidos entre 97 y 1003 es: {suma2}")
