"""
Entradas
Edad (str) -> split
Cantidad de años o meses (int) -> añ_ms_n
Mes o año (str) -> añ_ms
Genero (str) -> mh

Salidas
Resultado de la prueba (str) -> resultado

"""
#Entradas
edad = input("Ingrese su edad: ")
añ_ms_n, añ_ms = edad.split(" ") 
nv_hm = float(input("Ingresar nivel de hemoglobina: "))
mh = input("Ingresar genero: ")
añ_ms_n = int(añ_ms_n)
añ_ms = str (añ_ms)


#Caja negra
resultado=""

if ((añ_ms_n >= 0 and añ_ms_n <= 1) and (añ_ms == "mes" or añ_ms == "meses")): #0-1 mes
    if(nv_hm > 0 and nv_hm <13):
        resultado="Positivo"
    elif (nv_hm > 26):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if ((añ_ms_n > 1 and añ_ms_n <= 6) and (añ_ms == "mes" or añ_ms == "meses")):
    if(nv_hm > 0 and nv_hm <10):
        resultado="Positivo"
    elif (nv_hm > 18):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 6 and añ_ms_n <= 12) and (añ_ms == "meses")):
    if(nv_hm > 0 and nv_hm <11):
        resultado="Positivo"
    elif(nv_hm > 15):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 1 and añ_ms_n <= 5) and (añ_ms == "año" or añ_ms == "años")):
    if(nv_hm > 0 and nv_hm < 11.5):
        resultado="Positivo"
    elif(nv_hm > 15):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 5 and añ_ms_n <= 10) and (añ_ms == "años")):
    if(nv_hm > 0 and nv_hm < 12.6):
        resultado="Positivo"
    elif(nv_hm > 15.5):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 10 and añ_ms_n <= 15) and (añ_ms == "años")):
    if(nv_hm > 0 and nv_hm < 13):
        resultado="Positivo"
    elif(nv_hm > 15.5):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 15) and (añ_ms == "años") and (mh == "mujer" or mh == "Mujer")):
    if(nv_hm > 0 and nv_hm < 12):
        resultado="Positivo"
    elif(nv_hm > 16):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

if((añ_ms_n > 15) and (añ_ms == "años") and (mh == "hombre" or mh == "Hombre")):
    if(nv_hm > 0 and nv_hm < 14):
        resultado="Positivo"
    elif(nv_hm > 18):
        resultado="Negativo"
    else:
        resultado="Esta dentro del rango"

#Salidas
print(f"El resultado de su prueba de Anemia es: {resultado}.")