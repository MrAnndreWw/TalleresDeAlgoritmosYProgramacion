"""
Entradas
Nombre cliente (str) -> nc
Monto a pagar (float) -> mp

Salidas 
Monto a pagar con descuento (float) -> tp
Nombre cliente (str) -> nc

"""
#Entradas

nc = str (input("Ingresar nombre del cliente: "))
mp = float(input("Ingresar el monto a pagar: "))

#Caja negra

tp=""
ds=""

if (mp < 50000):
    tp = mp
elif (mp >= 50000 and mp < 100000):
    ds = mp*0.05
    tp = mp - ds
elif (mp >= 100000 and mp < 700000):
    ds = mp*0.11
    tp = mp - ds
elif (mp >= 700000 and mp < 1500000):
    ds = mp*0.18
    tp = mp - ds
elif (mp >= 1500000):
    ds = mp*0.25
    tp = mp - ds

#Salidas
print (f"Recibo del cliente {nc}:")
print (f"El monto de la compra es: {mp}")
print (f"El descuento recibido fue de: {ds}")
print (f"El total a pagar por {nc} es de: {tp}")