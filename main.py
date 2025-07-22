from math import factorial


class Program:
    @staticmethod
    def main():
        opcion=0
        while opcion!=8:
            print("""1. Calcular Factorial
            2. Suma de 'n' numeros naturales
            3. Calcular el n-esimo numero de fibonacci
            4. Contar cuantas veces aparece una letra en una palabra
            5. Invertir una cadena de texto
            6. Calcular la potencia de un numero base""")
            opcion=int(input("Ingrese la opcion: "))
            if opcion==1:
                n=int(input("Ingrese el numero a calcular el factorial: "))
                if n<0:
                    print("Ingrese un numero entero positivo")
                else:
                    print(Program.factorial(n))
            elif opcion==2:
                n=int(input("Ingrese numero limite"))
                print(Program.numeros_naturales(n))

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
Program.main()

