"""
Entradas
Precio final = float = pf
Precio de venta al publico = float = pvp

Salidas
Descuento aplicado = float = descuento
"""
#Entradas
pf = float(input("Ingresa el precio final del producto pagado: "))
pvp = float(input("Ingresar el precio del venta al publico del producto pagado: "))

#Caja negra
descuento = ((pvp-pf) / pvp) * 100

#Salidas
print(f"El descuento que se le aplico al producto fue del {round(descuento)}%")