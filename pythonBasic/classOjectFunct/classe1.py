# como crear una clase en python

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola me llamo {} y tengo {} años ".format(self.nombre, self.edad))


object1 = Persona("Marcela",25)

print(object1.saludar())

