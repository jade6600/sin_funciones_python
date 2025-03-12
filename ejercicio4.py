import random

#Definir función

contador_pares = 0

def calcular_promedio_pares(lista):
    suma = 0
    global contador_pares
    for i in lista:
        if i % 2 == 0:
            contador_pares += 1
            suma = suma + i
    promedio = suma / contador_pares
    print(f"hay {contador_pares} pares")
    return promedio


#input
#creamos lista vacia

lista = []

#Tamaño de la lista

n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,n)
    lista.append(num)

#processing

print(f"lista: {lista}")
print(f"el promedio de la lista es {calcular_promedio_pares(lista)}")