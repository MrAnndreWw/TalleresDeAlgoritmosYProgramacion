est={}
est.update({
        "1":{
            "nombre":"Lorea",
            "nota": 8
    },
        "2": {
            "nombre":"Markel",
            "nota": 4.2
    }, 
        "3": {
            "nombre":"Julien",
            "nota": 6.5
    }
})

listas=[]
listaa=[]
media=[]
for i in range(0,10):
    num=int(input("Numero de estudiante: "))
    prof=input("Nombre del estudiante: ")
    nota=float(input("Nota del estudiante: "))
    est.update({num:{"nombre":prof, "nota":nota}})
for key in est.keys():
    if (est[key]["nota"]<=5):
        listas.append(est[key]["nombre"])
    else:
        listaa.append(est[key]["nombre"])
    media.append(est[key]["nota"])
    s=sum(media)/(len(listas)+len(listaa))
print(listas)
print(listaa)
print("{:.1f}".format(s))