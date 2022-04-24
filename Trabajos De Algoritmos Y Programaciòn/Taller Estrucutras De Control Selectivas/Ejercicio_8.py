"""
Entradas
p (entero)
q (entero)

Salidas
Satisfacen la expresión -> r
"""
#Entradas
p = int(input("Ingresar el valor de p: "))
q = int(input("Ingresar el valor de q: "))

#Caja negra
r=""
t= (p**3) + (q**4) - (2*(p**2))

if(t > 680):
    r = print (f"{p} y {q} satisfacen la expresión.")
elif(t <= 680):
    r = print (f"{p} y {q} no satisfacen la expresión.")