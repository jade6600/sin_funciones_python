print(".......................................")
print("BUSCAR UN NUMERO CONJUNTO")
print("...........................................")

# entrada
b = int(input("Numero a buscar: ")) #se recibe el dato del usuario

# procesamiento
a = [1,2,3,4,5 ] #Se almacena una lista de datos
r = False #se inicia la variable r con un valor falso

for i in a:
    if i==b:
        print("Lo encontre")
        r = True
if r==False:
    print ("No lo encontre")

#salida

print("\nEso era...")

