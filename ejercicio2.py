#construir una funcion que reciba una cadena digitada(como parametro)por el usuario
# y que lo muetren veces en pantalla.El valor de n tambien es digitado por el usuario.

print("............................")
print("MOSTRAR CADENA N VECES")
print(".....................PANTALLA...............")
print("........................")

# definicion de la funcion
def mostrarCadena(cadena, n):
    for i in range(n):
        print(f"{i} . {cadena}")

#entrada
cadena = input("Digite la cadena a mostar: ")
n = int(input("Digite el numero de ves que quiere mostrar la cadena: "))

#procesamiento
mostrarCadena(cadena, n)

#salida
print("\nEso era...")