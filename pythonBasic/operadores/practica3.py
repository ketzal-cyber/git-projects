numeros = [1,2,3,4,5,6,7,8,9,10]
print("Lista de numeros: {}".format(numeros))

numero = int(input("Introduce un numero "))

if numero in numeros:
    print(" Si ")

if numero not in numeros:
    print( " No " )
