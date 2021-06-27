# Diccionarios que estn  indexados  no estan ordenados y se pueden modificar

diccionario = {"red":"rojo","blue":"azul","yellow":"amarillo"}

print(diccionario)

clave = input("Introduce la clave ")
elemento = input("Introduce el elemento ")
diccionario[clave] = elemento
print(diccionario)

valor = diccionario["yellow"]
print(valor)

# Borrar elemento
diccionario.pop("yellow")

del(diccionario["red"])

for llave, contenido in diccionario.items():
    print(llave, contenido)
