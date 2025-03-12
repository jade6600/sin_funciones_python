# Construir una funcion que reciba como parametro una lista de datos numericos y retor la suma de dichos datos
import random

print("...............................")
print("...................SUMA LISTA DATOS..................")
print("..........................................")
#definicion de la funcion
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma +i
    return suma

    
#entrada

#creamos una lista vacia
lista = []
# tamaño de la lista 
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

#procesamiento
print("Lista. ", lista)
print("la suma es: ", sumar_lista_datos(lista))

#salida
print("nEso\ era...")
    
      