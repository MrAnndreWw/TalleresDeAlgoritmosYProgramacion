#Entradas
b50k = int (input("Ingrese la cantidad de billetes de 50.000 que tiene el banco: "))
b20k = int (input("Ingrese la cantidad de billetes de 20.000 que tiene el banco: "))
b10k = int (input("Ingrese la cantidad de billetes de 10.000 que tiene el banco: "))
b5k  = int (input("Ingrese la cantidad de billetes de 5.000 que tiene el banco: "))
b2k  = int (input("Ingrese la cantidad de billetes de 2.000 que tiene el banco: "))
b1k  = int (input("Ingrese la cantidad de billetes de 1.000 que tiene el banco: "))
b500 = int (input("Ingrese la cantidad de billetes de 500 que tiene el banco: "))
b100 = int (input("Ingrese la cantidad de billetes de 100 que tiene el banco: "))

#Caja negra
tot_50k = 50000 * b50k
tot_20k = 20000 * b20k
tot_10k = 10000 * b10k
tot_5k  = 5000  * b5k
tot_2k  = 2000  * b2k
tot_1k  = 1000  * b1k
tot_500 = 500   * b500
tot_100 = 100   * b100

total_banco = tot_50k + tot_20k + tot_10k + tot_5k + tot_2k + tot_1k + tot_500 + tot_100

#Salidas
print(f"La cantidad de dinero que tiene el banco es de: {total_banco}")