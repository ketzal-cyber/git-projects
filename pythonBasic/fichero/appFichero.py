import moduloFicheros

nombre_file = "datos.txt"
#crear un objeto de la clase Fichero 
fichero = moduloFicheros.Fichero(nombre_file)

contenido = input("Ingrese contenido para incluir como cabecera a fichero")

fichero.grabarFichero(contenido)

salto ="\n"
contenido2 = input("Ingrese mas datos a incluir al file")
fichero.addDatoFile(salto+contenido2+salto)

texto_leido = fichero.leerFichero()

print(texto_leido)
