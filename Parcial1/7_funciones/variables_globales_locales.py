#Ejercicio 1
def calcular_area_perimetro(base, altura):
    
    area = 0
    perimetro = 0

    area = base * altura
    perimetro = base * 2 + altura * 2
    print(f"Un rectangulo con base {base } y altura {altura}, tiene un area de {area} y su perimetro de: {perimetro}")

base = int(input("Ingrese la base del rectangulo"))
altura = int(input("Ingrese la altura del rectangulo"))

calcular_area_perimetro(base,altura)

#Ejercicio 2
tareas_completadas = 0
tareas_incompletas = 0
tareas = 0

def mostrar_tareas_incompletas():
    print(f"Cuantas tareas tienes")

    print(f"Tienes un totsl de tareas:{tareas}, de las cuales realizaste{tareas_completadas} y tienes que hacer{tareas_incompletas}")

tareas=int(input("Ingrese la cantidad de tareas que tiene"))
tareas_completadas = int(input("Ingrese la cantidad de tareas que realizo"))

def completar_tareas():
    global tareas_completadas
    global tareas_incompletas
    tareas_incompletas = tareas - tareas_completadas

completar_tareas()
mostrar_tareas_incompletas()