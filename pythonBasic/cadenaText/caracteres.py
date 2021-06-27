# posision del caracter
caracteres = input(" Introduce la cade de caracteres que desees: ")
letra = caracteres[5]
final = caracteres[-1]
rango = caracteres[2:8]
tamanio = len(caracteres)
print(' El tamanio de la cadena de caracteres es: {}'.format(tamanio))
print(' caracter en la posision [5] es: '+ letra)
print(' caracter final [-1] es: '+ final)
print(' caracter en el rnago [2:8] es: '+ rango)

print(" cadena en mayusculas " + caracteres.upper())
print(" Cadena en minusculas "+ caracteres.lower())

print(" Formar una lista de un texto de caraceres ")
# funcion que permite separar palabras split(',') bajo un caracter de separacion
print(caracteres.split())

resultado = 10 / 3
print(" El resultado formateado es: {r:1.3f} ".format(r=resultado))

lenguaje = "Python"
version = 3
print(f" Lenguaje {lenguaje}, version {version} trabajando ")

