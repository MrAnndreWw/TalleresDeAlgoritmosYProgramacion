"""
Entradas
Lectura anterior (float) -> lmp
Lectura actual (float) -> lma

Salidas
Total a pagar -> ttp
"""
#Entradas
lmp = float(input("Ingresar la lectura anterior: "))
lma = float(input("Ingresar la lectura actual: "))

#Caja negra
if (lmp > lma):
    lct = lmp - lma
else:
    lct = lma - lmp

ttp=""
if (lct > 0 and lct <= 100):
    ttp = lct*4600
elif (lct >= 101 and lct <= 300):
    ttp = lct*80000
elif (lct >= 301 and lct <= 500):
    ttp = lct*100000
elif (lct >=501):
    ttp = lct*120000

#Salidas
print(f"El total a pagar este mes es de: {ttp}")