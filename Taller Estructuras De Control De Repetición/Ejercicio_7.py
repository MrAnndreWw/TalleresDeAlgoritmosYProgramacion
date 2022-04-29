while True:
    #Entradas
    datos=input()
    x, m=datos.split(" ")
    x=int(x)
    m=int(m)
    #Condicion de ciere
    if (x == 0 and m == 0):
        break
    #Caja negra
    r=x*m
    #Salida
    print(r)