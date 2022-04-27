"""
#Rompe una cadena
palabra="universidad"
for letra in palabra:
    if(letra=="e"):
        break
    print(letra)

#Continua sin la letra
palabra="universidad"
for letra in palabra:
    if(letra=="e"):
        continue
    print(letra)
"""
tupla=("Amarillo","Rosado","Azul","Rojo","Naranja","Verde","Gris")
#tamaño=len(tupla) #Muestra cuantas variables hay
#print(tamaño) 
#print(tupla[-1]) #Muestra el ultimo valor

for color in tupla:
    if (color[0]=="A"):
        print(color)