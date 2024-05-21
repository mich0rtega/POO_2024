# Hacer un programa que muestre todos los numero impares entre 2 y el numero que el usuario decida

num = int(input("Ingrese el numero limite"))

for num in range(2,num):
    if num % 3 == 0:
     print(num)