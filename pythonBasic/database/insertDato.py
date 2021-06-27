# insertar una fila de datos en la base de datos sqlite3
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('Noemi','Perez','Juarez',30)")

conexion.commit()
print('Fila insertada')

conexion.close()


