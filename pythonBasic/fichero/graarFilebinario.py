import pickle

lista_colores = ["azul","rojo","verde","amarillo"]

fichero = open("fichero_colores.pckl","wb")

pickle.dump(lista_colores,fichero)
fichero.close()

