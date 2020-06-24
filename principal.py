import numpy as np
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
a = 20 #En este caso tomamos que a y b valen 20 por eso lo colocamos de frente, sin que el usuario ingrese. Ademas seguira con el rango de 0 a 200
b = 20
print(crea_arreglo(a, b))#Imprimimos el arreglo con su nombre especifico y sus dos argumentos, si no, se producira un error

#No se hacer la parte 2 y 3. Por favor profesor podria explicar este problema en clase para una retroalimentación de como resolverlo.
import numpy as np
def mueve_col(a,z):   
    nueva = np.zeros((4,1))
    print(a)
    b = a[:,z]
    b = np.reshape(b,(4,1))
    hola = nueva + b
    print(hola)
    a[:,z]=a[:,1]
    a0 = a
    a0=np.delete(a0,1,axis=1)
    print(a0)
    luego = np.append(a0,hola,axis=1)
    return luego

def main():
    a = np.array([[34,43,73,25,10],
                  [82,22,12,14,10],
                  [53,94,66,84,10],
                  [35,73,24,34,10]])
    z = int(input('Ingrese el numero de columna: ')) #Solo aceptara 0, 1 o 2 por el tipo de matriz
    print(mueve_col(a,z))
if __name__ == "__main__":
    main()
