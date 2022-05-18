usuarios={
    "iperurena": {
            "nombre": "Iñaki",
               "apellido": "Perurena",
               "password": "123123"
          },
    "fmuguruza": {
            "nombre": "Fermín",
                "apellido": "Muguruza",
                "password": "654321"
          },
    "aolaizola": {
            "nombre": "Aimar",
                "apellido": "Olaizola",
                "password": "123456"
          }
     }
p=0
lista=[]
for key in usuarios.items():
    user=str(input("Ingrese su usuario: "))
    passw=int(input("Ingrese contraseña: "))
    lista.append(key)
    if user in lista and passw in lista: 
        p+=1
        print("incorrecto")
    else:
        print(usuarios[user]["nombre"])
        print(usuarios[user]["apellido"])
        break
    if(p==3):
        print("Cuenta bloqueada")
        break