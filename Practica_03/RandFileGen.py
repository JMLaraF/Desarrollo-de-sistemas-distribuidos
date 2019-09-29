import random #Generador de archivos con numeros random

n_archivos= int(input("¿Cuantos archivos deseas generar?"))
randfile = [None]*n_archivos
for j in range(0 , n_archivos ):
    randfile[j] = open("RandNums/RandomNums" + str(j) + ".txt", "w+" )
    for i in range(int(input('How many to generate?: '))):
        line = str(random.randint(1, 100)) + "\n"
        randfile[j].write(line)
    #print(line)
for j in range(0 , n_archivos ):
    randfile[j].close()
