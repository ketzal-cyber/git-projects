# actualizacion de datos en la base de datos sqlite3 y ordenarlos
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 40 WHERE nombre = 'Sandra'")


conexion.commit()

print('Fila actualizada')

conexion.close()
