"""
Entradas
Temperatura en grados Fahrenheit (int) -> tmp

Salidas
Deporte que debería practicar (str) -> dp
"""
#Entradas
tmp = int(input("Ingresar temperatura en grados fahrenheit: "))

#Caja negra
dp=""

if (tmp <= 10):
    dp = "Marcha"
elif (tmp > 10 and tmp <= 32):
    dp = "Esqui"
elif (tmp > 32 and tmp <= 70):
    dp ="Golf"
elif (tmp > 70 and tmp <= 85):
    dp = "Tenis"
elif (tmp > 85):
    dp = "Natación"

#Salidas
print(f"El deporte apropiado para practicar es: {dp}")