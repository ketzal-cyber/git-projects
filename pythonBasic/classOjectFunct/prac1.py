# ejercicio 1 de la creacio de  clases,objetos y funciones
class Coche:

    def __init__(self, marca, color, combustible, cilindraje):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindraje = cilindraje


    def mostrarCaracteristicas(self):
        print("Automovil de marca {} con color {} de combustible {} y con un cilindraje {} ".format(self.marca,self.color, self.combustible, self.cilindraje))


auto1 = Coche("Opel","rojo","gasolina","1.6")

auto1.mostrarCaracteristicas()
