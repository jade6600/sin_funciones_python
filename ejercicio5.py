# Construir una función que reciba como parámetro una lista de datos numéricos y retorne el promedio de los datos pares.

print("----------------------------------------------")
print("--------Promedio lista de datos pares---------")
print("----------------------------------------------")

import random

# Definición de la función
def promedio_lista_pares(lista):
   suma = 0
   n_p = 0
   for i in lista:
      if i%2== 0:
         suma = suma + i
         n_p = n_p + 1
   promedio = suma / n_p
   return promedio

# input
# Creamos una lista vacía
lista = []
# Tamaño de la lista
n_p = int(input("Dígite el tamaño de la lista: "))

for i in range(n_p):
    num = random.randint(2, 4)
    lista.append(num)

# processing
print("Lista: " , lista)
print("El promedio de la lista es: ", promedio_lista_pares(lista))