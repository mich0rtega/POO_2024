respuesta = input("¿Desea ingresar datos? (si/no): ")

contador = 0
acum_pacientes = 0

while respuesta.lower() == "si":
    nombre = input("Ingrese el nombre del paciente: ")
    sangre = input("Ingrese el tipo de sangre: ")
    medicion_sis1 = int(input("Ingrese la medicion sis 1: "))
    medicion_dia1 = int(input("Ingrese la medición dia 1: "))
    medicion_sis2 = int(input("Ingrese la medicion sis 2: "))
    medicion_dia2 = int(input("Ingrese la medicion dia 2: "))
    medicion_sis3 = int(input("Ingrese la medición sis 3: "))
    medicion_dia3 = int(input("Ingrese la medicion dia 3: "))
    medicion_finalsis = int(input("Ingrese la medicion final: "))
    medicion_finaldia = int(input("Ingrese la medicion final: "))


    promedio_presionsis = int((medicion_sis1 + medicion_sis2 + medicion_sis3)/3)
    print(f"Promedio presion sistolica: {promedio_presionsis}")
    promedio_presiondia = int((medicion_dia1 + medicion_dia2 + medicion_dia3)/3)
    print(f"Promedio presion sistolica: {promedio_presiondia}")

    promedio_final_sis = int((promedio_presionsis + medicion_finalsis)/2)
    promedio_final_dia = int((promedio_presiondia + medicion_finaldia)/2)
    print(f"Promedio total sis: {promedio_final_sis}")
    print(f"Promedio total dia: {promedio_final_dia}")

    if promedio_final_sis <=120 and promedio_final_dia <=80:
     print("Presenta presion normal")
    

    contador += 1
    acum_pacientes+=contador

    respuesta = input("¿Desea ingresar más datos? (si/no): ")

Pacientes_ingresados = acum_pacientes - 1
print(f"Pacientes ingresados: {Pacientes_ingresados}")
