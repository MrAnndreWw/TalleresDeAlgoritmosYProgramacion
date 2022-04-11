"""
Entradas
monto presupuestado = float = mpp

Salidas
Presupuesto ginecologia = float = pg
Presupuesto traumatologia = float = pt
Presupuesto Pediatria = float = pp
"""
#Entradas
mpp = float (input("Ingresar el monto presupuestado: "))

#Caja negra
pg = mpp * 0.40
pt = mpp * 0.30
pp = mpp * 0.30

#Salidas
print(f"El presupuesto anual que tendra el area de ginecologia es de: {pg}")
print(f"El presupuesto anual que tendra el area de traumatologia es de: {pt}")
print(f"El presupuesto anual que tendra el area de pediatria es de: {pp}")