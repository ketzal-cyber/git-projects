# insertar varias filas de datos en la base de datos sqlite3
import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

# generar una lista con los datos a insertar
lista_personas = [ ('Sandra','Cano','Rosas',25),('Violeta','Sanchez','ortiz',29),('Luisa','Ortaga','Gomez',30)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()
print(' 3 Filas insertadas')

conexion.close()

