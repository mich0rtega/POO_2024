"""
List (Array)

son colecciones o conjunto de datos/valores bajo 
un mismo nombre, para acceder a los valores se
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable permite miembros duplicados
"""

#Ejemplo 1: Crear una lista con valores num enteros e imprimir la lista
# numeros=[23,34]
# print(numeros)

# #Recorrer la lista con un for
# for i in numeros:
#     print(i)

#Recorrer la lista con un while
# i = 0
# while i < len(numeros): #saca el total de los elementos de una lista
#     print(numeros[i])       
#     i +=1


#Ejemplo 2 crear una lista de palabras, posteriormente ingresar una palabra
# para buscar la coincidencia en la lista e indicar si aparece la palabra y en que posicion
#en caso contraio indicar una sola vez si no lo encontro

# palabras= ["hola","2024","10.23","True"]
# print(palabras)
# palabra_buscar = input("Ingrese la palabra a buscar")
# no_encontro = True
# for i in palabras:
    
#     if palabra_buscar == i:
#         print(f"Encontre la palabra {palabra_buscar}, en la posicion:{palabras.index(i)}") #index es buscar posicion
#         no_encontro = False

# if no_encontro:
#   print(f"No se encontro la palabra dentro de la lista")
    
# i = 0
    
# while i < len(palabras):
#     if palabra_buscar == palabras[i]:
#         print(f"Encontré la palabra {palabra_buscar}, en la posición: {i}")
#         no_encontro = False
#     i += 1
    
# if no_encontro:
#     print(f"No se encontró la palabra dentro de la lista")

#Ejemplo 3 Crear una lista multilinea o multidimensional (matriz) para crear una agenda telefonica
# agenda = [
#    ["Carlos", 6181234567],
#    ["Fernando", 618738268],
#    ["Matias", 6691112233],
#    ["Juan Polainas",6182332345]
# ]
# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#Ejemplo 4 Crear un programa que permita gestionar (administrar)
#peliculas, colocar un menu de opciones para agregar,
#remover, consultar peliculas

#Notas
#1. Utilizar funciones y mandar llamar desde otro archivo
#2 Utilizar listas para almacenar los nombres de las peliculas
from funciones_peliculas import *
import os

os.system("cls")

while True:
    print(".:::CINEMAX:::. \n 1.- Agregar \n 2.- Remover \n 3.- Consultar \n 4.- Actualizar \n 5.- Buscar \n 6.- SALIR ")
    opcion = input("\tElige una opción:").upper()

    if opcion == "1" or opcion == "AGREGAR":
        agregarPeliculas()
        print("\n")
    elif opcion == "2" or opcion == "REMOVER":
        eliminarPeliculas()
        print("\n")
    elif opcion == "3" or opcion == "CONSULTAR":
        consultarPeliculas()
        print("\n")
    elif opcion == "4" or opcion == "ACTUALIZAR":
        actualizarPeliculas()
        print("\n")
    elif opcion == "5" or opcion == "BUSCAR":
        buscarPeliculas()
        print("\n")
    elif opcion == "6" or opcion == "SALIR":
        print("Gracias por usar el programa, adios")
        break
    else:
        print("Opción no válida Por favor intente de nuevo.")
        espereTecla()
