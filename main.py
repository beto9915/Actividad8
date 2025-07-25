from math import factorial

from comtypes.tools.tlbparser import char_type


class Program:
    @staticmethod
    def main():
        opcion=0
        while opcion!=7:
            print("""1. Calcular Factorial
            2. Suma de 'n' numeros naturales
            3. Calcular el n-esimo numero de fibonacci
            4. Contar cuantas veces aparece una letra en una palabra
            5. Invertir una cadena de texto
            6. Calcular la potencia de un numero base
            7. Salir""")
            opcion=int(input("Ingrese la opcion: "))
            if opcion==1:
                n=int(input("Ingrese el numero a calcular el factorial: "))
                if n<0:
                    print("Ingrese un numero entero positivo")
                else:
                    print(Program.factorial(n))
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==2:
                n=int(input("Ingrese numero limite"))
                print(Program.numeros_naturales(n))
            elif opcion==3:
                n=int(input("Ingrese numero para calcular Fibonacci"))
                print(Program.fibonacci(n))
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==4:
                palabra=input("Ingresa la palabra: ")
                letra=char_type(input("Ingrese la letra a buscar: "))
                print(Program.letras_en_palabra(palabra, letra))
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==5:
                cadena=input("Ingrese cadena de texto: ")
                print(Program.invertir(cadena))
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==6:
                base=input("Ingrese el numero base: ")
                exponente=input("Ingrese el exponente: ")
                print(Program.base_exponente(base, exponente))
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==7:
                print("Gracias por usar mi programa, me costo mucho hacerlo...")
            else:
                print("No es un numero valido, intente de nuevo...")
                print("\npresione ENTER para continuar...")
                input()

    @staticmethod
    def factorial(n):
        if n==0:
            return 1
        else:
            return n*Program.factorial(n-1)
    @staticmethod
    def numeros_naturales(o):
        if o==1:
            return 1
        else:
            return o + Program.numeros_naturales(o-1)
    @staticmethod
    def fibonacci(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return n+Program.fibonacci(n-1)
    @staticmethod
    def letras_en_palabra(palabra,letra):
        if palabra=="":
            return 0
        suma = 1 if palabra[0]==letra else 0
        return suma + Program.letras_en_palabra(palabra[1:], letra)
    @staticmethod
    def invertir(cadena):
        if cadena<=1:
            return cadena
        else:
            ultima_palabra=cadena[-1]
            resto=Program.invertir(cadena[:-1])
            return ultima_palabra+resto
    @staticmethod
    def base_exponente(base, exponente):
        if exponente==0:
            return 1
        else:
            return base*Program.base_exponente(base, exponente-1)
Program.main()

