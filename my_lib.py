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
import numpy as np
def mueve_col():   
                   #0 #1 #2 #3 #4 ----> en columna
    a = np.array([[34,43,73,25,10], #indice 0 en fila 
                  [82,22,12,14,10], #indice 1 en fila
                  [53,94,66,84,10], #indice 2 en fila
                  [35,73,24,34,10]]) #indice 3 en fila   
    nueva = np.zeros((4,1))
    print(a)
    b = a[:,0]
    b = np.reshape(b,(4,1))
    hola = nueva + b
    print(hola)
    a[:,0]=a[:,1]
    a0 = a
    a0=np.delete(a0,1,axis=1)
    print(a0)
    luego = np.append(a0,hola,axis=1)
    return luego
print(mueve_col())
