"""
Entradas
Lote de naranjas = int = x
Valor de la docena = float = y
Dinero ganado = float = k

Salidas
Porcentaje de ganancia = float = pg
"""
#Entradas
x = int(input("Ingresar el lote de naranjas: "))
y = float(input("Ingresar el valor de la docena: "))
k = float(input("Ingresar el dinero ganado en la inversion: "))

#Caja negra
n=(x/12)*6
p=(k-n)
pg=(p*100)/n

#Salida
print(f"El porcentaje de ganancia obtenida es de {pg}%")