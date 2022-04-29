listaco=[]
lista_agr=[]
lista_ron=[]
lista_cer=[]
lista_teq=[]
lista_whi=[]
lista_otr=[]
lista_mujermenor=[]
lista_hombreagua2025=[]
suma_edad=0
cantida_cer=0
while True:
    consume=int(input("¿Consume licor? Digite 1 para si y 2 para no: "))
    if(consume==1):
        licor_fav=int(input("¿Licor preferido? \n 1.Aguardiente \n 2.Ron \n 3.Cerveza \n 4.Tequila \n 5.Whisky \n 6.Otro \nRespuesta: "))
        edad = int(input("¿Cual es su edad?: "))
        sexo = int(input("¿Cual es su genero? \n 1.Hombre \n 2.Mujer\nRespuesta: "))
        continuar_encuesta=int(input("¿Desea continuar la encuesta? Digite 1 para si y 2 para no: "))

    #Consume licor
    if(consume==1):
        listaco.append(consume)
        #Licor favorito
        if(licor_fav==1):
            lista_agr.append(licor_fav)
        elif(licor_fav==2):
            lista_ron.append(licor_fav)
        elif(licor_fav==3):
            lista_cer.append(licor_fav)
        elif(licor_fav==4):
            lista_teq.append(licor_fav)
        elif(licor_fav==5):
            lista_whi.append(licor_fav)
        elif(licor_fav==6):
            lista_otr.append(licor_fav)
    #Mujer menor
        if (sexo==2):
            if(edad < 18):
                lista_mujermenor.append(sexo)
    #Hombres que no consumen aguardiente entre 20 y 25 años
        if(licor_fav!=1):
            if(sexo==1):
                if(edad>=20 and edad<=25):
                    lista_hombreagua2025.append(1)
    #Promedio de edad de personas que consumen cerveza
        if(licor_fav==3):
            suma_edad=suma_edad+edad
            cantida_cer=cantida_cer+1
        if(continuar_encuesta==2):
            por_cerveza=suma_edad//cantida_cer
    #Porcentaje de personas que consumen whisky
        if(continuar_encuesta==2):
            por_whisky=((len(lista_whi))*100)/(len(listaco))

        if(continuar_encuesta==2):
            print(f"La cantidad de personas que consumen licor es: {len(listaco)}")
            print(f"La cantidad de mujeres menores de edad es: {len(lista_mujermenor)}")
            print(f"La cantidad de hombres que no consumen aguardiente que tienen entre 20 y 25 años es: {len(lista_hombreagua2025)}")
            print(f"El promedio de edad de personas que consumen cerveza es de: {por_cerveza}")
            print(f"El porcentaje de personas que toman whisky es de: {por_whisky}")
            break