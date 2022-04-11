import math
#Entradas
a = float(input("Ingresar lado a:"))
b = float(input("Ingresar lado b:"))
c = float(input("Ingresar lado c:"))
#Caja negra
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#Salidas
print(f"El area del triangulo es: {round(area)}")