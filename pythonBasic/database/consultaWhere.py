
# consultar de datos en la base de datos con where sqlite3
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad < 30")

personas_seleccionadas = cursor.fetchall()

for persona in personas_seleccionadas:
    print(persona)


print('Consulta con where realizada')

conexion.close()

