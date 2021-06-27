
# Borrado de datos en la base de datos sqlite3
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Luisa'")

conexion.commit()

print('Fila borrada')

conexion.close()
