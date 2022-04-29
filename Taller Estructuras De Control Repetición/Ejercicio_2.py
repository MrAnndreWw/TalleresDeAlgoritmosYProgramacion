"""
Entradas
c (int) -> c

Salidas
Numeros impares que no son divisibles de 7 hasta 100 (int)
"""
#Caja negra while
print("Repetición en while: ")
c = 1
while (c<=100):
    if (c%2 == 0 or c%7 == 0):
        c=c+1
    else:
        print(c)
        c = c+1

#Caja negra for
print("Repetición en for: ")
for c in range (1, 101,2):
    if (c%7 == 0):
        continue
    print(c)
