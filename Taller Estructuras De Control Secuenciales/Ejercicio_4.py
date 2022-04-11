"""
Entradas
Valor inicial = float = valor_ini

Salidas
Pago total = float = totalpagar
"""
#Entradas
valor_ini = int(input("Ingresa el valor a pagar sin descuento"))
#Caja negra
descuento = (valor_ini*15)/100 #float
totalpagar = valor_ini - descuento #float
#Salidas
print(f"el valor total a pagar con el descuento es de: {round(totalpagar)}")