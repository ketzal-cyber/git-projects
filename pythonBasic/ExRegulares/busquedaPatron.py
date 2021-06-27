# Expreciones regulares (search, findall, split, sub

cadena = "Esto es una cadena de caracteres para utilizar la funcionalidad search"

import re

resultado = re.search('cadena',cadena)
if (resultado):
    print('cadena encontrada')
else:
    print('Cadena no encontrada')

# buscar si la cadena finaliza con una determinada palabra 
resultado2 = re.search('funcionalidad$', cadena)
print(resultado2)

# buscar si la cadena empieza con una determinada palabra
resultado3 = re.search('^Esto',cadena)
print(resultado3)

cadena2 = "Segunda linea de texto para buscar patrones"
# buscar conjunto de palabras dentro de la cadena 
# investigar el funcionaminento 
#resultado4 = re.search("linea.*buscar".cadena2)

# findall
cadena4 = """
El lenguaje mi es java,
el lenguaje tuyo es c#,
el lenguaje de el es python,
el lenguaje de ella es c++
el lenguaje suyo es java
"""


result = re.findall("lenguaje.*java", cadena4)
print(result)   # devuellve una lista de las concidencias

#split
cadena5 = "Esto es una cadena para el uso de la funcionalidad split en python"
res = re.split("\s",cadena5)
print(res)  # devuelve una lista de las palaras que conponene la cadena de caracteres

# sub
result2 = re.sub("python","NodeJS",cadena5)
print(result2)





