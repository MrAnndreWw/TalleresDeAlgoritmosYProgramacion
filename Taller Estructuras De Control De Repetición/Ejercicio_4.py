"""
Entradas
c (int)
c2 (int)

Salidas
Suma total while (int) -> suma
Termino doceavo while (int) -> termino
Suma total for (int) -> suma2
Termino doceavo for (int) -> termino2 
"""
#Caja negra while
print("Repetición en while: ")
termino=1
c=6
suma=0
while (c<=61):
    print(c)
    if(termino==12):
        print(f"El termino doceavo es: {c}")
    suma=suma+c
    c=c+5
    termino=termino+1
print(f"La suma total de los números es: {suma}")

#Caja negra for
print("Repetición en for: ")
suma2=0
termino2=1
for c2 in range (6,62,5):
    print(c2)
    if(termino2==12):
        print(f"El termino doceavo es: {c2}")
    suma2= suma2+c2
    termino2=termino2+1
print(f"La suma total de los números es: {suma2}")