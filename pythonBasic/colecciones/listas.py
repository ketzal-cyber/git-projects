# Tema de las listas y su manejo en python
lista = ["Practicar Python", "Practicar OracleDB", "Leer reealacion de DB","jugar play"]
elemento = input("Introduce su tarea ")
lista.append(elemento)
lista.remove("jugar play")

# ciclo or para recorrer la lista
for temas in lista:
    print(temas)
