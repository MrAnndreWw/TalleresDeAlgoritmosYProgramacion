"""
Entradas 
k (int) -> k
n (float) -> n

Salidas
Número de terminos while (int) -> cantidad
Número de terminos for (int) -> cantidad2
"""
#Caja negra while
print("Repetición en while: ")
k=1
n=0
cantidad=0
while (n<=999):
    n=(k**2+1)/k
    cantidad=cantidad+1
    print(n)
    k=k+1
print(f"El numero de terminos que hay es de: {cantidad}")

#Caja negra for
print("Repetición en for: ")
k=1
cantidad2=0
for n2 in range (1,999,1):
    n2=(k**2+1)/k
    cantidad2=cantidad2+1
    print(n2)
    k=k+1
print(f"El numero de terminos que hay es de: {cantidad}")