#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aprobaron y cuantos 
#no aprobaron 


for alumno in range(1,16):
    calif = int(input("Ingrese calificacion del alumno: "))
    if calif < 80:
        print("Reprobado")
    else:
         print("Aprobado")
    