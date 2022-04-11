"""
Entradas
Precio a contado = float = pcon
Precio a cuotas = float = pcuo

Salidas
Porcentaje de cobro = float = pc
"""
#Entradas
pcon = float(input("Ingresar el precio del computador a contado: "))
pcuo = float(input("Ingresar el precio de la cuota del computador: "))

#Caja negra
pc = (pcon/12) - pcuo

#Salidas
print(f"El porcentaje que se cobra por el recargo es de: {pc}")