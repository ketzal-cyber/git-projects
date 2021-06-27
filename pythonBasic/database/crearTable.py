# creacionde una tabla en la base de datos sqlite3

import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apepat TEXT, apemat TEXT, edad INTEGER)")

conexion.commit()

print('Table creada en sqlite3')
conexion.close()

