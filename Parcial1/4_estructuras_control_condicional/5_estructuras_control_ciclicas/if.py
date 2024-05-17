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

# Ejemplo 1 (if simple)
color = input("Ingresa un color: ")
if color == "rojo":
    print("Soy el color rojo")

# Ejemplo 2 (if compuesto)
color = input("Ingresa un color: ")
if color == "rojo":
    print("Soy el color rojo")
else:
    print("No soy color rojo, soy otra cosa")

# Ejemplo 3 (if anidado)
color = input("Ingresa un color: ")
if color == "rojo":
    print("Soy el color rojo")
elif color != "rojo":
    print("No soy color rojo, soy otra cosa")

# Ejemplo 4 (if y elif)
color = input("Ingresa un color: ")
if color == "rojo":
    print("Soy el color rojo")
elif color == "amarillo":
    print("Soy el color amarillo")
elif color == "azul":
    print("Soy el color azul")
else:
    print("No soy ningún color")

# Programa para solicitar el número de la semana
dia = input("Ingrese el día de la semana (1 al 7): ")
if dia == "1":
    print("Lunes")
elif dia == "2":
    print("Martes")
elif dia == "3":
    print("Miércoles")
elif dia == "4":
    print("Jueves")
elif dia == "5":
    print("Viernes")
elif dia == "6":
    print("Sábado")
elif dia == "7":
    print("Domingo")
else:
    print("Número de día inválido")
