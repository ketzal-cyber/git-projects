
# consulta de datos en la base de datos sqlite3 y ordenarlos
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

lista_personas_ordenada = cursor.fetchall()

for persona in lista_personas_ordenada:
    print(persona)



print('Fila insertada')

conexion.close()

