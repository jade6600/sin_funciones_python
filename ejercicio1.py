print("------------------------------")
print("- MOSTRAR NOMBRE EN PANTALLA -")
print("------------------------------")

#Definicion de la funcion 
def mostrarNombre(nombre):
    """print(f"1, {nombre}")
    print(f"2, {nombre}")
    print(f"3, {nombre}")
    print(f"4, {nombre}")
    print(f"5, {nombre}")"""

    for i in range (1,6):
        print(f"{1} . {nombre}")


# Entrada
nombre = input("Digite su nombre: ")

# Procesamiento
mostrarNombre(nombre)

#Salida
print("\nEso era...")