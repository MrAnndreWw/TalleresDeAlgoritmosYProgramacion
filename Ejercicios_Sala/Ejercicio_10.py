"""
Entradas 
Numero de estudiantes (int) -> n

Salidas

"""
n = int(input("Digite cantidad de estudiantes: "))

altura_mayor=0

for i in range (1,n+1):
    #Entrada
    altura = float(input("Digite la altura del estudiante: "))
    #Caja negra
    if (altura_mayor<=altura):
        altura_mayor=altura
print(altura_mayor)