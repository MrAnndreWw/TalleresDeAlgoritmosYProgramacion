"""
Entradas
Salario (float) -> sa

Salidas 
Salario despuès de aumento (float) -> ss
"""
#Entradas
sa = float(input("Ingresar su salario: "))

#Caja negra
amt=""
ss=""

if (sa < 900000):
    amt = sa*0.15
    ss = amt + sa
elif (sa > 900000):
    amt = sa*0.12
    ss = amt + sa

#Salidas
print (f"Su salario sera de {ss}")