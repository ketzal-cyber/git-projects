# admin de Tareas

from io import open

# Funcion para abrir fichero
def abrirFile():
    fichero = open("tarea.txt","a")
    
    fichero.close()
# end funcion    

#Abriendo fichero
file = open("tareas.txt","r+")

tarea = input("Introduce una nueva tarea: ")

file.write(tarea)

# Leyendo contenido del fichero
contenido = file.readlines()

# Imprimiendo contenido
print("contenido: {} \n".format(contenido))

#Cerrando fichero
file.close()