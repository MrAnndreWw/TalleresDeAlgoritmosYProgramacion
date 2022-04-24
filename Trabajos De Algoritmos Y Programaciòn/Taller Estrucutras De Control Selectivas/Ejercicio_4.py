"""
Entradas 
Monto a pagar (float) -> map

Salidas
Invertido por la empresa (float) -> dn_em
Credito fabricante (float) -> tot_cr_fb
Intereses credito fabricante (float) -> in_cr_fb
Credito bancario (float) -> ps_bn
"""
#Entradas
map = float(input("Ingresar el monto total a pagar: "))

#Caja negra
dn_em=""
ps_bn="No hay prestamo bancario"
cr_fb=""

if(map > 5000000):
    dn_em = map*0.55
    ps_bn = map*0.30
    cr_fb = map*0.15

elif(map < 5000000):
    dn_em = map*0.70
    cr_fb = map*0.30

in_cr_fb = cr_fb*0.20
tot_cr_fb = in_cr_fb + cr_fb

#Salidas
print(f"El total invertido por la empresa es de: {dn_em}")
print(f"El total a pagar al credito del fabricante es de: {tot_cr_fb}")
print(f"El total a pagar por intereses al credito del fabricante es de: {in_cr_fb}")
print(f"El total pagar al prestamo del banco es de: {ps_bn}")