from funciones_compartir import *
import os

os.system("cls")

peliculas=[]

def agregarPeliculas():
    pelicula = input("ingrese la pelicula")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas():
    pelicula = input("ingrese la pelicula a eliminar")
    peliculas.remove(pelicula)
    espereTecla()

def consultarPeliculas():
    print(f"Lista de películas:{peliculas}")
        

def actualizarPeliculas():
    actu = input("Ingrese el nombre de la película a actualizar: ")
    if actu in peliculas:  
        nueva_pelicula = input("Ingrese el nuevo nombre de la película: ")
        index = peliculas.index(actu)  
        peliculas[index] = nueva_pelicula  
    else:
        print(f"Película: {actu} no encontrada.")  
    espereTecla()  

def vaciarPelicula():
    peliculas.clear
    espereTecla()
    
def buscarPeliculas():
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        print(f"Película: {pelicula} encontrada")
    else:
        print(f"Película: {pelicula} no encontrada")
    espereTecla()


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
