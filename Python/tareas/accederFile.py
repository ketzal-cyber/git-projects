# admin de Tareas

#Abriendo fichero
file = open("tareas.txt","r+")

tarea = input("Introduce una nueva tarea: ")

file.write(tarea)

# Leyendo contenido del fichero
contenido = file.readline()

# Imprimiendo contenido
print("lineas del fichero \n"+ contenido)

#Cerrando fichero
file.close()