"""
Entradas
Primera edad = int = primera_edad
Segunda edad = int = segundad_edad
Tercera edad = int = tercera_edad

Salidas
Promedio = float = promedio
"""
#Entradas
primera_edad = int(input("Ingresar primera edad"))
segunda_edad = int(input("Ingresar segunda edad"))
tercera_edad = int(input("Ingresar tercera edad"))
#Caja negra
promedio = (primera_edad+segunda_edad+tercera_edad)/3 #float
#Salidas
print("El promedio es: ",promedio)
#print("El promedio es: " + str(promedio))
#print(f"El promedio es: {promedio}")