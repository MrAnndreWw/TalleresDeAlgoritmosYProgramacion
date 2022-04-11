"""
Entradas
nombre trabajador = str = nt
numero de horas trabajadas = int = ht
pago por hora = float = ph
numero de horas extras = int = he
total de hijos = int = th

Salidas
sueldo neto = float = sn
asignaciones = float = a
deducciones = float = d
"""
#Entradas
nt = str(input("Ingresar el nombre del trabajador: "))
ht = int (input("Ingresar el numero de horas trabajadas: "))
ph =  float(input("Ingresar pago por horas: "))
he = int(input("Ingresar número de horas extra: "))
th = int (input("Ingresar cantidad de hijos: "))

#Caja negra
sue_tot_h = ph * ht
pag_he = ph * 0.25
he_t = ph + pag_he
sue_tot_he = he_t * he
sueldo = sue_tot_h + sue_tot_he

deduccion = sueldo * 0.14
asignaciones = 250000 + (173000 * th) + 180000
sueldo_neto = sueldo - deduccion + asignaciones

#Salidas
print(f"Las asignaciones tienen un valor de: {asignaciones}")
print(f"Las deducciones tienen un valor de: {deduccion}")
print(f"El sueldo total de {nt} para el mes de diciembre es: {sueldo_neto}")