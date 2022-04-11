"""
Entradas
Cantidad de galones = float = cg

Salidas
Cobro al cliente = float = cc
"""
#Entradas
cg = float (input("Ingrese la cantidad de galones comprados por el cliente: "))

#Caja negra
gpl = (cg * 3785)
cc = (gpl * 50000)

#Salidas
print (f"El cobro que debe realizarse al cliente por la compra es de: {cc}")