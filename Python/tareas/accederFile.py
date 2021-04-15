# admin de Tareas

#Abriendo fichero
file = open("tareas.txt","w")

# Leyendo contenido del fichero
contenido = file.read()

# Imprimiendo contenido
print("lineas del fichero \n"+ contenido)

#Cerrando fichero
file.close()