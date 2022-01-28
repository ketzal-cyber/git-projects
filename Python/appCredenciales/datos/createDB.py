#Creacion de la base de datos para palabras clave

import sqlite3

conexion = sqlite3.connect("palabra.db")

print('Creada base de datos')

conexion.close()
