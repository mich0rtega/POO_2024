# Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo)
# de los 60 primero numero naturales resolverlo con while y for 

#For 
acumulador = 0
for num in range (0,61):
    cuadrado = num * num
    print(f"num: {num}, cuadrado: {cuadrado}")
    acumulador+= num
    

#while
i = 0
while i <= 60:
     cuadrado_while = i * i
     print(f"num: {i}, cuadrado: {cuadrado_while}")
     i+=1
     
