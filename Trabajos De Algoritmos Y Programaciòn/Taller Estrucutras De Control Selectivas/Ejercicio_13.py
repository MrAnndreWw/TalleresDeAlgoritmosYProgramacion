"""
Entradas
Día nacimiento (int) -> dian
Mes nacimiento (int) -> mesn
Año nacimiento (int) -> añon
Mes actual (int) -> mesa
Año actual (int) -> añoa

Salidas
Signo de la persona (str) -> signo
Edad de la persona (int) -> edad 
"""

#Entradas
dian=int(input("Ingrese el dia de su nacimiento: "))
mesn=int(input("Ingrese el mes de su nacimiento: "))
añon=int(input("Ingrese el año de su nacimiento: "))

mesa=int(input("Ingrese el mes actual: "))
añoa=int(input("Ingrese el año actual: "))
#Caja Negra
signo=""

#Hallar signo
if (mesn == 11 and dian >= 22 or mesn == 12 and dian <= 21):
    signo="Sagitario"

if (mesn == 12 and dian >= 22 or mesn == 1 and dian <= 20):
    signo="Capricornio"

if (mesn == 1 and dian >= 21 or mesn == 2 and dian <= 19):
    signo="Acuario"

if (mesn == 2 and dian >= 20 or mesn == 3 and dian <= 19):
    signo="Piscis"

if (mesn == 3 and dian >=21 or mesn == 4 and dian <= 20):
    signo="Aries"

if (mesn == 4 and dian >= 21 or mesn == 5 and dian <= 21):
    signo="Tauro"

if (mesn == 5 and dian >= 22 or mesn == 6 and dian <= 21):
    signo="Geminis"

if (mesn == 6 and dian >= 22 or mesn == 7 and dian <= 22):
    signo="Cancer"

if (mesn == 7 and dian >= 23 or mesn == 8 and dian <= 23):
    signo="Leo"

if (mesn == 8 and dian >= 24 or mesn == 9 and dian <= 22):
    signo="Virgo"

if (mesn == 9 and dian >= 23 or mesn == 10 and dian <= 22):
    signo="Libra"

if (mesn == 10 and dian >= 23 or mesn == 11 and dian <= 21):
    signo="Escorpion"

#Calcular edad
if  mesn>mesa:
    edad=(añoa-añon)-1
else:
    edad=(añoa-añon)

#Salidas
print(f"El signo de la persona es: {signo}")
print(f"La edad de la persona es: {edad}")