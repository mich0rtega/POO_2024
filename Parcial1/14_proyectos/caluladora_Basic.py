import os
from funciones_compartir import espereTecla

def solicitarNumeros(cantidad):
    if cantidad == 2:
        n1 = int(input("Numero #1: "))
        n2 = int(input("Numero #2: "))
        return n1, n2
    elif cantidad == 1:
        n1 = int(input("Numero: "))
        return n1,

def calculadora(n1, n2=None, opcion=None):
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "^" or opcion == "POTENCIA":
        return f"{n1} ** {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        return f"√{n1} = {n1 ** 0.5}"

os.system("cls")
opcion = True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia\n 6.- Raiz\n 7.- Salir")
    opcion = input("\t Elige una opción: ").upper()
    if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4' or opcion == '5':
        n1, n2 = solicitarNumeros(2)
        print(calculadora(n1, n2, opcion))
    elif opcion == '6':
        n1, = solicitarNumeros(1)
        print(calculadora(n1, opcion="RAIZ"))
    elif opcion == '7':
        opcion = False
        print("Gracias por utilizar el sistema ...")
    espereTecla()
