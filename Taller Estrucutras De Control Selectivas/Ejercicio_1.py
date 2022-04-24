"""
Entradas
Cantidad de dinero en el banco (float) -> ctd
Porcentaje de interes (float) -> prc

Salidas
Cantidad de dinero generada (float) -> ctg
"""
#Entradas
ctd = float(input("Ingresar cantidad de dinero en el banco: "))
prc = float(input("Ingresar porcentaje de interes: "))

#Caja negra
in_dn = ((ctd*prc)/100)

ctg=""
if (in_dn > 100000):
    ctg = in_dn + ctd
else:
    ctg = ctd

#Salidas
print(f"La cantidad de dinero generada es: {ctg}")