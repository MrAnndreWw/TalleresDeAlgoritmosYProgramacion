"""
Entradas 
cantidad de hombres = int = hombres
cantidad de mujeres = int mujeres

Salidas
Porcentaje mujeres y hombres = int
"""
#Entradas
mujeres = int(input("Ingresar cantidad de mujeres")) #int
hombres = int(input("Ingresar cantidad de hombres")) #int
#Caja negra
total_estudiantes = hombres + mujeres #int
mp = mujeres*100/total_estudiantes #float
hp = hombres*100/total_estudiantes #float
#Salidas
print (f"El porcentaje de mujeres es: {round(mp)} y el de porcentaje de hombres es: {round(hp)}") #str
