alc=0
gas=0
die=0
while True:
    #Entradas
    x = int(input())
    #Condiciones
    if (x==1):
        alc=alc+1
    elif(x==2):
        gas=gas+1
    elif(x==3):
        die=die+1
    #Condicion de cierre
    elif(x==4):
        break
#Salidas
print("MUITO OBRIGADO")
print("Alcool:",alc)
print("Gasolina:",gas)
print("Diesel:",die)