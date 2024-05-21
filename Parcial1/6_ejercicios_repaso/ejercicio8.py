#Hacer un programa que resuelva lo siguiente: cuanto es x por ciento de x numero?

num_porce = int(input("Ingrese el porcentaje de calcular"))
num = int(input("Ingrese el numero a sacar el porcentaje"))


porcentaje = (num_porce/100)*num
print(f"El {num_porce}% de {num} es: {porcentaje}")