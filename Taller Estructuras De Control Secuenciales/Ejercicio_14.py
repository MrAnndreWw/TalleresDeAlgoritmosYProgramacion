"""
Entradas
Lectura mes pasado = float = lmp
Lectura mes actual = float = lma
Valor kilovatio = float = vk

Salidas
Total pago = float = tp
"""
#Entradas
lmp = float(input("Ingresar la lectura del mes pasado: "))
lma = float(input("Ingresar la lectura del mes actual: "))
vk = float(input("Ingresar el valor por kilovatio: "))

#Caja negra
tp = (lmp + lma) * vk

#Salidas
print (f"El monto total a pagar por la luz electrica es: {tp}")