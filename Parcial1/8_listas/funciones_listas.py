paises = ["Mexico","USA","Brasil","China"]
numeros = [100,80,3.1416,75]
varios =["UTD",True,100,0.100]

#Ordenar la listas 
print(paises) 
paises.sort()
print(paises)

print(numeros) 
numeros.sort()
print(numeros)

# print(varios) # no se puede ordenar varios
# varios.sort()
# print(varios)

#Agregar elementos a la lista
print(numeros)
numeros.append(100) #agregar elementos
print(numeros)
numeros.insert(len(numeros),200) #Hay que contar posiciones y agg un valor como parametro
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2) #borra el de la posicion
print(numeros)

#Dar la vuelta a los elementos de una lista
print(varios)
varios.reverse()

#Buscar un valor o un dato dentro de una lista
encontro = "Brasil" in paises
print(encontro)

#Vaciar una lista
print(paises)
paises.clear()
print(paises)

#Unir listas
print(varios)
varios.extend(numeros)
print(varios)