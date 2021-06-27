class Fichero:

    def __init__(self, nombre):
        self.nombre = nombre

# leer funcion leer fichero  rt
    def leerFichero(self):
        readFile = open(self.nombre,"rt")
        datoFichero = readFile.read()
        return datoFichero

# crear funcion grabar fichero wt
    def grabarFichero(self, parametro):
        saveFile = open(self.nombre,"wt")

        contenidoSave = parametro

        saveFile.write(contenidoSave)

        saveFile.close()

# agregar funcion para incluir fichero para agregar datos al fichero al final at
    def addDatoFile(self, contenidoNew):
        agregarDatos = open(self.nombre, "at")

        agregarDatos.write(contenidoNew)

        agregarDatos.close()


