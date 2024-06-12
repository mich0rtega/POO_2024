#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#a.- Recorrer la lista y mostrarla
#b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#c.- ordenarla y mostrarla
#d.- mostrar su longitud
#e.- buscar algun elemento que el usuario pida por teclado

lista = [1,8,3,5,7,2,4,6]

#a.- Recorrer la lista y mostrarla
print(f"\n Recorrer lista y mostrarla")
def recorrerMostrar():
   for i in lista:
    print(i)
recorrerMostrar()


#b.- hacer una funcion que recorra la lista de numeros y devuelva un string
print(f"\n Hacer una funcion que recorra la lista de numeros y devuelva un string")

def devuelveString():
   i = 0
   while i < len(lista): 
      recorrer =  print(f"Hay un total de 8 elementos, los cuales son: {lista[i]}")
      i +=1
   
   return recorrer
devuelveString()

#c.- ordenarla y mostrarla
print(f"\n ordenarla y mostrarla")
def ordenarMostrar():
  lista.sort()
  print (lista)
ordenarMostrar()

#d.- mostrar su longitud
print(f"\n  mostrar su longitud")
def longitudLista():
 print(len(lista))
longitudLista()

#e.- buscar algun elemento que el usuario pida por teclado
print(f"\n  buscar algun elemento que el usuario pida por teclado")

i = 0
num_buscar = int(input("Ingrese el num a buscar"))
no_encontro = True

def buscarElemento():
 if num_buscar in lista:
    print(f"Encontré el num {num_buscar}")
    no_encontro = False

 if no_encontro:
  print(f"No se encontró el num dentro de la lista")
buscarElemento()