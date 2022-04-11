#Entradas Matemáticas
exa_mat = float(input("Ingresar nota del examen de matemáticas"))
ta1_mat = float(input("Ingresar nota de la tarea uno de matemáticas"))
ta2_mat = float(input("Ingresar nota de la tarea dos de matemáticas"))
ta3_mat = float(input("Ingresar nota de la tarea tres de matemáticas"))
#Entradas Fisica
exa_fis = float(input("Ingresar nota del examen de fisica"))
ta1_fis = float(input("Ingresar nota de la tarea uno de fisica"))
ta2_fis = float(input("Ingresar nota de la tarea uno de fisica"))
#Entradas Química 
exa_qui = float(input("Ingresar nota del examen de química"))
ta1_qui = float(input("Ingresar nota de la tarea uno de química"))
ta2_qui = float(input("Ingresar nota de la tarea dos de química"))
ta3_qui = float(input("Ingresar nota de la tarea tres de química"))
#Caja negra Promedio
promedio_mat = exa_mat*0.90 + ((ta1_mat+ta2_mat+ta3_mat)/3)*0.10
promedio_fis = exa_fis*0.80 + ((ta1_fis+ta2_fis)/2)*0.20
promedio_qui = exa_qui*0.85 + ((ta1_qui+ta2_qui+ta3_qui)/3)*0.15
promedio_gen = (promedio_mat + promedio_fis + promedio_qui)/3
#Salidas
print(f"El promedio de todas las materias es: {promedio_gen}")
