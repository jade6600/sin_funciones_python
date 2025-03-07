print("................................")
print("BUSCAR UN NUMERO EN CONJUNTO")
print("...............................")

#definicion de la funcion
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i ==datoABuscar:
            r = True
    return r

#entrada
dato = int(input("Numero a buscar: ")) #se recibe el dato del usuario

#procesamiento 
lista = [1,2,3,4,5] #se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("Lo encontre")
else:
    print("No lo encontre")

#Salida