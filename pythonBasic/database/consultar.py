
# consultar datos en la base de datos sqlite3
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()
for  persona in personas:
    print(persona)

print('Consulta realizada')

conexion.close()

