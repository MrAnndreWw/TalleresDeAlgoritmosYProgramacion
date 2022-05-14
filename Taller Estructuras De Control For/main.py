archivo = open('paises.txt', 'r',)
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M  
"""
lista=[]
ciudad=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    contador = contador + 1
    print(i)  
print (contador)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
lista2=[]
ciudades=[]
paisu=[]
for i in archivo:
  e=i.index(":")
  for q in range(e+2, len(i)-1):
    lista.append(i[q])
    e="".join(lista)
  ciudades.append(e)
  lista=[]
  n=i.index(":")
  for t in range(0, n):
    lista2.append(i[t])
    n="".join(lista2)
  paisu.append(n)
  lista2=[]
for i in paisu:
  if(i[0]=="U"):
    print(i) 
for i in ciudades:
  if(i[0]=="U"):
    print(i)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
contador = 0
for i in archivo:
  contador = contador + 1
print(contador)
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
singapur=[]
for i in archivo: 
  p=i.index(":")
  for g in range(p+2, len(i)-1):
    lista.append(i[g])
    p="".join(lista)
  singapur.append(p)
  lista=[]
for i in singapur:
  if(i=="Singapur"):
    print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
for i in archivo: 
    if(i=="Venezuela: Caracas\n"):
      print(i)   
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
ciudades=[]
contador=0
for i in archivo:
  if(i[0]=="E"):
    a = i.index(":")
    for r in range (a+2,len(i)-1):
      ciudades.append(i[r])
    a="".join(ciudades)
    print(a)
    ciudades=[]
    contador=contador+1
print(contador)
"""
#Busque e imprima la Capiltal de Colombia
"""
bogota=[]
for i in archivo:
  if (i[0]=="C"):
    a = i.index(":")
    for r in range (a+2,len(i)-1):
      bogota.append(i[r])
    b="".join(bogota)
    bogota=[]
    if(b=="Bogotá"):
      print(b)
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  x=" ".join(lista)
  c=c+1
  if(x=="México: Ciudad de México \n"):
    break
  lista=[]
print(c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
paises=[]
for i in archivo:
  lista.append(i)
lista.remove("Madagascar: rey julien\n")
lista.insert(109,"Madagascar: Antananarivo\n")
for e in lista:
  paises.append(e)
u = "".join(paises)
print (u)
"""
archivo.close()
#Agregue un país que no esté en la lista 
"""
pais = "Kosovo: Pristina"
archivo2 = open("paises.txt", "a")
archivo2.write("\n" + pais + "\n")
archivo2.close()
"""