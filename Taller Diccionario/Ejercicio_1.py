lista=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
numeros={}
for i in lista: 
    key=str(i) 
    a=lista.count(i)
    numeros.update({key:a})
print(numeros)