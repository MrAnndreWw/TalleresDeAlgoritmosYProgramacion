"""
Entradas
Salario = float = salario_nt

Salidas
Salario total = float = salario_tot
"""
#Entradas
salario_nt = int(input("Ingresar el salario: "))
#Caja negra
salario_tot = salario_nt * 0.8
#Salidas 
print (f"Su salario neto es: {round(salario_tot)}")
