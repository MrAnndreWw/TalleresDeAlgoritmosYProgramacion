"""
Entradas
sueldo del trabajador (float) -> st

Salidas
Categoria (int) -> ct
Nuevo saldo bruto (float) -> ns 
"""
#Entradas
st = float(input("Ingresar el sueldo del trabajador: "))

#Caja negra
ct=""
ns=""

if(st == 900000):
    ct = 5
    amt = st*0.60
    ns = st + amt
elif (st == 2000000):
    ct = 4
    amt = st*0.40
    ns = st + amt
elif (st == 3600000):
    ct = 3
    amt = st*0.20
    ns = st + amt
elif (st == 4300000):
    ct = 2
    amt = st*0.15
    ns = st + amt
elif ( st == 5000000):
    ct = 1
    amt = st*0.10
    ns = st + amt

#Salidas
print(f"La categoria del trabajor es {ct} y su nuevo sueldo es de: ${ns} ")