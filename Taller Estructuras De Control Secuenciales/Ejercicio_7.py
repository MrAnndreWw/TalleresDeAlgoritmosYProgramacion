"""
Entradas
metros = int = cant_met

Salidas
Pulgadas = float = pulgadas
Pies = float = pies
"""
#Entradas
cant_met = int(input("Ingresa los metros: "))
#Caja negra
pulgadas = cant_met * 39.27
pies = pulgadas / 12
#Salidas
print ("la conversion de metros a pulgadas es: {:.2f}".format(pulgadas))
print ("la conversion de metros a pies es: {:.2f}".format(pies))