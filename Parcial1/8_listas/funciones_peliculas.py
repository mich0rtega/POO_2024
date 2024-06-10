def espereTecla():
        print("Oprime cualquier tecla para continuar")
        input()

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


    
def buscarPeliculas():
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        print(f"Película: {pelicula} encontrada")
    else:
        print(f"Película: {pelicula} no encontrada")
    espereTecla()