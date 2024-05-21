#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el primer numero"))

for numero in range(num, num2 + 1):
  print(f"Números entre {num} y {num2}:")
  print(numero)