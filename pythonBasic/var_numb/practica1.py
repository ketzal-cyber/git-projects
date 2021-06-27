number = int(input(" Introduce un numero "))
decimal = float(input(" Introduce un numero decimal "))
cadena = input(" Introdue una cadena de caracteres " )

print(type(number))
print(type(decimal))
print(type(cadena))

print(" La suma de los tres numeros es: ")
suma = number + decimal + int(cadena)
print(' La suma es: {}'.format(suma))
print(type(suma))

