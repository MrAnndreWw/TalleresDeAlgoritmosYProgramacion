"""
Entradas
Kilometros (float) -> km

Salidas
Total a pagar (float) -> tp
"""
#Entradas
km = float(input("Ingresar la cantidad de kilometros: "))

tp=""
if (km > 300 and km < 1000):
    kmr = km - 300
    tkp = kmr *  30000
    tp = tkp + 70000
elif (km > 1000):
    kmr2 = km - 1000
    tkp2 = kmr2 * 9000
    tp = tkp2 + 150000
else:
    tp = 50000
#Salidas
print(f"El total a pagar es: ${tp}")