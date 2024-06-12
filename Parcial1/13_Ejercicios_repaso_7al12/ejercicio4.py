# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = [1,2,3]

cadena = "Hola que tal"

entero = 56

logico = True

def mensajeLista(lista):
    print(f"Esta es una lista, {lista}{type}")
mensajeLista(lista)

def mensajeCadena(cadena):
    print(f"Esta es una cadena: , {cadena}{type}")
mensajeCadena(cadena)

def mensajeEntero(entero):
    print(f"Este es un número entero:, {entero}{type}")
mensajeEntero(entero)

def mensajeLogico(logico):
    print(f"Este es un valor lógico:, {logico}{type}")
mensajeLogico(logico)