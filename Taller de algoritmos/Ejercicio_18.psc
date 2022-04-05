Algoritmo Ejercicio_18
	Escribir "Ingrese su primer nombre"
	Leer PrimerNombre
	Escribir "Ingrese su primer apellido"
	Leer PrimerApellido
	Escribir "Ingrese su segundo apellido"
	Leer SegundoApellido
	PrimerLetra<-Subcadena(PrimerNombre,1,1)
	SegundaLetra<-Subcadena(PrimerApellido,1,1)
	TerceraLetra<-Subcadena(SegundoApellido,1,1)
	Escribir "Las iniciales de cada nombre son: " Mayusculas(PrimerLetra) Mayusculas(SegundaLetra) Mayusculas(TerceraLetra)
FinAlgoritmo
