"""
Entradas
Valor de k (int) -> k
Valor de n (int) -> n

Salidas
Numero en contador desde n hasta k (int)
"""
#Entradas
k=int(input("Ingresar el valor de K: "))
n=int(input("Ingresar el valor de N: "))
#Caja negra while
if (k<n):
    while(n>=k):
        print (n)
        n = n-1
        if(n == k-1):
            break
    print("El programa termino")
else:
    print("El valor de K debe ser menor que el valor de N.")


#Caja negra for
if(k<n):
    for n in range (n, k-1 ,-1):
        print(n)
else:
    print("El valor de K debe ser menor que el valor de N.")
