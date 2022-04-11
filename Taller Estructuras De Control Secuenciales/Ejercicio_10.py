"""
Entradas
chelines austriacos = ca
dracmas griegos = drg
pesetas = pes

Salidas
Chelines austriacos a pesetas = cp
Dragmas griegos a francos franceses = df
Pesetas a dolares = pd
Pesetas a liras italianas = pl
"""
#Entradas
ca = float(input("Ingresar cantidad de chelines austriacos: "))
drg = float(input("Ingresar cantidad de dracmas griegos: "))
pes = float(input("Ingresar cantidad de pesetas: "))

#Caja negra
cp = ca * 9568.71
df = drg * 886.07 / 20110
pd = pes / 122499
pl = pes / (9289/100)

#Salidas
print ("Los chelines austriacos en pesetas es: {:.2f}".format(cp))
print ("Los dragmas griegos en francos franceses es: {:.2f}".format(df))
print ("Las pesetas en dolares es: {:.2f}".format(pd))
print ("Las pesetas en liras italianas es: {:.2f}".format(pl))
