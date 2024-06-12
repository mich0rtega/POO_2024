#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas


lista = []

def llenado(lista):
    if lista == []:  
        print("La lista está vacía. Ingrese palabras o frases.")
        while True:
            palabra = input("Ingresa una palabra o terminar para acabar el programa: ")
            if palabra.lower() == "acabar":
                break
            lista.append(palabra)
    return lista

def mayusculas(lista):
    for elemento in lista:
        print(elemento.upper())


lista = llenado(lista)

print("La lista final es:", lista)
print("Los elementos de la lista en mayúsculas son:")
mayusculas(lista)
