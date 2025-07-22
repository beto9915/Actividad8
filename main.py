from math import factorial


class Program:
    def static(main):
        opcion=0
        while opcion!=8:
            print("""1. Calcular Factorial
            2. Suma de 'n' numeros naturales
            3. Calcular el n-esimo numero de fibonacci
            4. Contar cuantas veces aparece una letra en una palabra
            5. Invertir una cadena de texto
            6. Calcular la potencia de un numero base""")
            opcion=int(input("Ingrese la opcion: "))
            if (opcion==1):
                n=int(input("Ingrese el numero a calcular el factorial: "))
                if n<0:
                    print("Ingrese un numero entero positivo")
                else:
                    print(factorial(n))
            elif(opcion==2):
                n=int(input("Ingrese numero limite"))
                print(numeros_naturales(n))


            def factorial(n):
                if n==0:
                    return 1
                else:
                    return n*factorial(n-1)
            def numeros_naturales(n):
                if n==1:
                    return 1
                else:
                    return n+numeros_naturales(n-1)


