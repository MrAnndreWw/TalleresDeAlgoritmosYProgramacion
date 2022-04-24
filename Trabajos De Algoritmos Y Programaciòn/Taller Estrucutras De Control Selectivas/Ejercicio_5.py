"""
Entradas
Ganancias primer departamento (float) -> g1
Ganancias segundo departamento (float) -> g2
Ganancias tercer departamento (float) -> g3
Salario bruto mensual trabajadores (float) -> sb

Salidas
Salario primer departamento (float) -> s1
Salario segundo departamento (float) -> s2
Salario tercer departamento (float) -> s3
"""
#Entradas
from telnetlib import SB


g1 = float(input("Ingresar las ganancias del primer departamento: "))
g2 = float(input("Ingresar las ganancias del segundo departamento: "))
g3 = float(input("Ingresar las ganancias del tercer departamento: "))
sb = float(input("Ingresar el salario bruto mensual: "))

#Caja negra
gt = g1 + g2 + g3
gtp = gt * 0.33

st1=""
st2=""
st3=""

if (g1 > gtp):
    sbp = sb * 0.20
    st1 = sb + sbp
elif (g1 <= gtp):
    st1 = sb

if (g2 > gtp):
    sbp = sb * 0.20
    st2 = sb + sbp
elif (g2 <= gtp):
    st2 = sb

if (g3 > gtp):
    sbp = sb * 0.20
    st3 = sb + sbp
elif (g3 <= gtp):
    st3 = sb

#Salidas
print(f"El salario del primer departamento es: {st1}")
print(f"El salario del segundo departamento es: {st2}")
print(f"El salario del tercer departamento es: {st3}")