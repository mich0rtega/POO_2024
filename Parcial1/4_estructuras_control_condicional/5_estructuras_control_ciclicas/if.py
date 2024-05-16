"""
Existe una estructura de condicion llamada "if"
la cual evalua una condicion para encontrar el valor "True" y si se cumple
la condicion se ejecuta la linea o lineas de codigo

Tienes 4 variantes de if

1. if simple
2. if compuesto
3. if anidado
4. if y elif

"""

#Ejemplo 1 if simple
color = input("Inhresa un color: ")
if color=="rojo":
  print ("Soy el color rojo")

  
#Ejemplo 2 if compuesto
color = input("Inhresa un color: ")
if color == "rojo":
  print ("Soy el color rojo")
else:
  print ("No soy color rojo, soy otra cosa")


 #Ejemplo 3 if anidado
color = input("Inhresa un color: ")
if color == "rojo":
  print ("Soy el color rojo")
if color != "rojo":
#else:
 print ("No soy color rojo, soy otra cosa")

 #Ejemplo 4 if y elif
color = input("Inhresa un color: ")
if color == "rojo":
  print ("Soy el color rojo")
elif color =="amarillo":
  print("Soy el color amarillos")
elif color == "azul":
  print("Soy el color azul")
else:
 print("No soy ningun color")

 #Ejemplo: crear un programa que solicite el numero de la semana 
 # e imprima en pantalla el dia que le corresponde

 dia = input("Ingrese el dia de la semana")

if dia == "1":
  print("Lunes")
elif dia == "2":
  print("Martes")
elif dia == "3":
  print("Miercoles")
elif dia == "4":
   print("Jueves")
elif dia == "2":
  print("Martes")
elif dia == "3":
  print("Miercoles")
elif dia == "4":
   print("Jueves")
   


  
  