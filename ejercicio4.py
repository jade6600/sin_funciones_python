# una funcion 

import random

print("...............................")
print("...................SUMA LISTA DATOS..................")
print("..........................................")
#definicion de la funcion
def calcular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio
    

    
#entrada

#creamos una lista vacia
lista = []
# tamaño de la lista 
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

#procesamiento
print("Lista: ", lista)
print("el promedio de la lista es : ", calcular_promedio_lista(lista))

#salida
print("nEso\ era...")