sino = int(input("¿Desea iniciar el programa? \n 1.Si \n 2.No \n Respuesta: "))
#Puntaje Alto
puntajealt = 0
nompuntalt = ""
#Puntaje Bajo
puntajebaj = 0
nompuntbaj = ""
#Promedio Puntaje
puntajep = 0
#Inferior al promedio
inf = []
#Superior al promedio
sup = []
if(sino == 1):
    num_estudiantes=int(input("Ingresa la cantidad de estudiantes: "))

    for i in range(0,num_estudiantes):
       pe = input()
       nombre, puntaje= pe.split(" ")
       nombre=str(nombre)
       puntaje=int(puntaje)
       puntajep = puntajep + puntaje
       puntajeprom = puntajep/num_estudiantes
    
       #Puntaje más alto
       if(puntaje > puntajealt):
           puntajealt=puntaje
           nompuntalt=nombre
        #Puntaje más bajo
       if(puntaje < puntajealt or puntaje<puntajebaj):
            puntajebaj = puntaje
            nompuntbaj = nombre
        #Inferior al promedio
       if(puntaje < puntajeprom):
            inf.append(puntaje)
        #Superior al promedio
       if(puntaje > puntajeprom):
           sup.append(puntaje)

    #Inf al promedio
    porinf = (len(inf)*100)/num_estudiantes
    #Sup al promedio
    porsup = (len(sup)*100)/num_estudiantes
    print(f"El estudiante con el puntaje más alto es: {nompuntalt}")
    print(f"El estudiante con el puntaje más bajo es: {nompuntbaj}")
    print(f"El puntaje maximo obtenido es: {puntajealt}")
    print(f"El puntaje minimo obtenido es: {puntajebaj}")
    print("El promedio del puntaje es:",("{0:.2f}".format(puntajeprom)))
    print("El porcentaje de estudiantes con puntajes inferiores al promedio es:",("{0:.0f}".format(porinf)+str("%")))
    print("El porcentaje de estudiantes con puntajes superiores al promedio es:",("{0:.0f}".format(porsup)+str("%"))) 
elif(sino == 2):
    print("Programa no ejecutado.")