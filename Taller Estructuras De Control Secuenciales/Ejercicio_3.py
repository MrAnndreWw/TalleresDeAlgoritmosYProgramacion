"""
Entradas
sueldo base = int = sueldo_base
primera venta = int = venta1 
segunda venta = int = venta2
tercera venta = int = venta3

Salidas
sueldo total = float = totalsueldo
"""
#Entradas
sueldo_base = int(input("Ingresar sueldo base"))
venta1 = int(input("Ingresar primera venta"))
venta2 = int(input("Ingresar segunda venta"))
venta3 = int(input("Ingresar tercera venta"))
#Caja negra
totalventas = venta1 + venta2 + venta3
comision = (totalventas*10)/100
totalsueldo = comision + sueldo_base
#Salidas
print(f"El total ganado entre sueldo base y comision por ventas es: {round(totalsueldo)}")