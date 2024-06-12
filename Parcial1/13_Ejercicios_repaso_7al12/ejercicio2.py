#2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []
i = 0
while len(lista) < 120:
    num = int(input("ingrese el num"))
    lista.append(num)
    print(lista)
    i+=1

for i in range(1,121):
    num = int(input("ingrese el num"))
    lista.append(num)
    print(lista)
    i+=1