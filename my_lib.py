#Función 1
import random
from random import randint
def crea_arreglo(a, b):    #Creamos el nombre de la función como se solicita y los dos argumentos que representaran filas y columnas
    arreglo = []    #Arreglo es el nombre de mi arreglo valga la rebundancia
    for i in range(a):
        arreglo.append([0]*b)   
    for i in range(a):
        for j in range(b):
            arreglo[i][j] = randint(0, 200) #Tengo considerado el rango de 0 a 200 que rellenaran mi matriz random
    return arreglo
a = int(input('Ingrese el número de columnas deseadas: '))
b = int(input('Ingrese el número de filas deseadas: '))
print(crea_arreglo(a, b))#Imprimimos el arreglo con su nombre especifico y sus dos argumentos, si no, se producira un error

#Función 2
