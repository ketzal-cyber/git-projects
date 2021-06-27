# cmanejo de contenido JSon convertir
#convertir datos de un diccionario python a una estructura JSON
import json

producto1 = {"nombre":"silla","color":"blanco","precio":100}
print('Diccionario: {}'.format(producto1))
nombre = producto1["nombre"]
print('llave del diccionario {}'.format(nombre))

ojectJSon = json.dumps(producto1)
print(ojectJSon)

objeto = ojectJSon[2]
print("Objeto json acceder al nombre {}".format(objeto))

# convertir una estructura JSON a un diccionario de python
jsonAdicc = json.loads(ojectJSon)
print('convertir un json a un diccionario en python')
print("resultado: {}".format(jsonAdicc))

