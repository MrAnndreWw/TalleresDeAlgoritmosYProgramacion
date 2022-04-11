"""
Entradas
dinero = float = dinero

Salidas
Ganancia = float = ganancia
Total de ganancias = float = total
"""
#Entradas
dinero = int(input("Ingresar la cantidad de dinero"))
#Caja negra
ganancia = (dinero*2)/100
total = ganancia + dinero
#Salidas
print(f"La ganancia de cada mes es: {ganancia}")
print(f"Lo total obtenido con ganacia y inversión es: {total}")