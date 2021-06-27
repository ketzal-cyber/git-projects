# crear una base de datos desde python

import sqlite3

conexion = sqlite3.connect("basedatos1.db")

print('Creada base de datos')

conexion.close()


