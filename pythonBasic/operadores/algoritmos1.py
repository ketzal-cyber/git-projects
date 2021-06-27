# Variable de tipo numerico para realizar incisos
# uso de operadores aritmeticos logicos, de asignacion de comparacion
while(True):
    print()
    print("|------------------------------------------------------------------|")
    print(" Resolver los incisos "+
        "\n a.- Escrie los valores en orden inverso "+
        "\n b.- Escribe los valores en orden inverso omitiendo el segundo"+
        "\n c.- Calcular la funcion (a + b - c) / d "+
        "\n d.- Calcular la funcion ( a - b )* 2 / c  -  ( a - b )*3 / d/a "+
        "\n z.- Salir")
    salir = input("Introduce una letra de inciso ")
    if salir == 'z' or salir == 'Z':
        break
    elif salir == 'a':
        a = int(input("Introduce un valor "))
        b = int(input("Introduce un valor "))
        c = int(input("Introduce un valor "))
        d = int(input("Introduce un valor "))
        print(" Valores introducidos: {}, {}, {}, {}. ".format(d,c,b,a))
    elif salir == 'b':
        a = int(input("Introduce un valor "))
        b = int(input("Introduce un valor "))
        c = int(input("Introduce un valor "))
        d = int(input("Introduce un valor "))
        print(" Valores introducidos invertidos omitiendo el segundo {}, {}, {}. ".format(d,c,a))
    elif salir == 'c':
        #"\n c.- Calcular la funcion (a + b - c) / d "+
        a = int(input("Introduce un valor "))
        b = int(input("Introduce un valor "))
        c = int(input("Introduce un valor "))
        d = int(input("Introduce un valor "))
        operBasic = (a + b - c) / d
        print(" El resultado de la operacion \t ( a={} + b={} - c={} ) / d={} es: {}".format(a,b,c,d,operBasic))
    elif salir == 'd':
        #"\n d.- Calcular la funcion ( a - b )* 2 / c  -  ( a - b )*3 / d/a "+
        a = int(input("Introduce un valor "))
        b = int(input("Introduce un valor "))
        c = int(input("Introduce un valor "))
        d = int(input("Introduce un valor "))
        operacion = (( a - b ) * 2 ) / c - (( a - b ) * 3 ) / d / a
        sustrac1 = a - b
        producto1 = sustrac1 * 2
        divicion1 = producto1 / c
        resto1 = producto1 % c
        cociente1 = producto1 // c
        print(" El resultado de la funcion \t (( a={} - b={} )* 2 ) / c={}  - (( a={} - b={} )* 3 ) / ( d={} / a={} ) es = {}".format(a,b,c,a,b,d,a,operacion))
        print(" Resultado por pasos es: (( a - b ={} *2 ={} / c  ={} ".format(sustrac1,producto1,divicion1))
        print("resto de la divion es: {}, cociente de la divicion es: {} ".format(resto1,cociente1))
    else:
        print("Debe ingresar una letra de inciso ")

