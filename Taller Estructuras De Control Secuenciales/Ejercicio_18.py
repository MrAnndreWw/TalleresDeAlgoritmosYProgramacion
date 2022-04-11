"""
Entradas
Cantidad de prestamo = float = cp

Salidas
porcentaje anual = float = pa
"""
#Entradas
cp=int(input("Ingrese la cantidad del prestamo: "))

#Caja negra
pa=(cp*4)/100

#Salidas
print(f"El porcentual anual es de: {pa}")