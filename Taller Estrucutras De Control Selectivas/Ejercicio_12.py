"""
Entrada
Cantidad de dinero (float) -> cd

Salida
Dinero final (str) -> df
"""
#Entrada
cd=float(input("Ingrese la cantidad entera de dinero: "))

#Caja negra
dinero= list()

for i in (100000, 50000, 20000,10000, 5000, 2000, 1000, 500, 200, 100, 50):
    if cd >= i:
        dinero.append(int(cd/i)*i)
        cd=cd-int(cd/i)*i
    else: 
        cd=cd
df=str(dinero)[1:-1]

#Salida
print("La cantidad es: ", df)