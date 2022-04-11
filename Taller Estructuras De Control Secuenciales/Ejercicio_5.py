"""
Entradas
Primer calificacion parcial = int = pr_par1
Segunda calificacion parcial = int = pr_par2
Tercera calificacion parcial = int = pr_par3
Examen final = int = exfinal
Trabajo final = int = tbfinal
"""
#Entradas
pr_par1 = int(input("Ingresar primer calificacion parcial: "))
pr_par2 = int(input("Ingresar segunda calificacion parcial: "))
pr_par3 = int(input("Ingresar tercera calificacion parcial: "))
exfinal = int(input("Ingresar calificacion del examen final: "))
tbfinal = int(input("Ingresar calificacion del trabajo final: "))
#Caja negra
pro_tra = (pr_par1 + pr_par2 + pr_par3)/3
nota_tra = pro_tra * 0.55
nota_ex = exfinal * 0.30
nota_tb = tbfinal * 0.15
nota_total = nota_tra + nota_ex + nota_tb
#Salidas
print(f"El promedio de la materia es de: {round(nota_total)}")