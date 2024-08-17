from  Medicos import medico
from Enfermeros import enfermero
from Paciente import paciente
from funciones import *
import getpass


def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro Médico
          2.- Registro Enfermero
          3.- Login Médico
          4.- Login Enfermero
          5.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1':
            registrar_medico()
        elif opcion == '2':
            registrar_enfermero()
        elif opcion == '3':
            login_medico()
        elif opcion == '4':
            login_enfermero()
        elif opcion == '5':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def registrar_medico():
    borrarPantalla()
    print("\n \t ..:: Registro de Médico ::..")
    nombre = input("\t ¿Cuál es tu nombre?: ")
    apellidos = input("\t ¿Cuáles son tus apellidos?: ")
    numEmpleado = input("\t Ingresa tu numero de empleado: ")
    password = getpass.getpass("\t Ingresa tu contraseña: ")
    especialidad = input("\t ¿Cuál es tu especialidad?: ")
    turno = input("\t Ingrese el turno: ")
    obj_medico = medico.Medico(nombre, apellidos, numEmpleado, password, especialidad,turno)
    if obj_medico.registrar():
        print(f"\n \t {nombre} {apellidos}, se registró correctamente, con el numero: {numEmpleado}")
    else:
        print(f'\n \t**Por favor vuelva a intentarlo más tarde, no fue posible insertar el registro**...')
    esperarTecla()

def registrar_enfermero():
    borrarPantalla()
    print("\n \t ..:: Registro de Enfermero ::..")
    nombre = input("\t ¿Cuál es tu nombre?: ")
    apellidos = input("\t ¿Cuáles son tus apellidos?: ")
    numEmpleado = input("\t Ingresa tu numero de empleado: ")
    password = getpass.getpass("\t Ingresa tu contraseña: ")
    area = input("\t ¿Cuál es tu área?: ")
    turno = input("\t Ingrese el turno: ")
    obj_enfermero = enfermero.Enfermero(nombre, apellidos, numEmpleado, password, area,turno )
    if obj_enfermero.registrar():
        print(f"\n \t {nombre} {apellidos}, se registró correctamente, con el numero: {numEmpleado}")
    else:
        print(f'\n \t**Por favor vuelva a intentarlo más tarde, no fue posible insertar el registro**...')
    esperarTecla()

def login_medico():
    borrarPantalla()
    print("\n \t ..:: Inicio de Sesión Médico ::..")
    numEmpleado = input("\t Ingresa tu numero de empleado: ")
    password = getpass.getpass("\t Ingresa tu Contraseña: ")
    registro = medico.Medico.login(numEmpleado, password)
    if registro:
        menu_medico(registro)
    else:
        print(f"\n \t Email o contraseña incorrectos, vuelva a intentarlo")
        esperarTecla()

def login_enfermero():
    borrarPantalla()
    print("\n \t ..:: Inicio de Sesión Enfermero ::..")
    numEmpleado = input("\t Ingresa tu numero de empleado: ")
    password = getpass.getpass("\t Ingresa tu Contraseña: ")
    registro = enfermero.Enfermero.login(numEmpleado, password)
    if registro:
        menu_enfermero(registro)
    else:
        print(f"\n \t Email o contraseña incorrectos, vuelva a intentarlo")
        esperarTecla()

def menu_medico(medico_tuple):
    medico_obj = medico.Medico(
        nombre=medico_tuple[1],
        apellidos=medico_tuple[2],
        numEmpleado=medico_tuple[3],
        password='',  \
        especialidad='', 
        turno=medico_tuple[5]
    )
    while True:
        borrarPantalla()
        print(f"""
        .:: Menú Médico ::.
        Bienvenido(a) Dr. {medico_tuple[1]} {medico_tuple[2]}
        1.- Registrar Paciente
        2.- Registrar Diagnóstico y Receta
        3.- Ver Paciente
        4.- Cerrar Sesión
        """)
        opcion = input("\t Elige una opción: ").upper()
        
        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            registrar_diagnostico_y_receta(medico_obj)
        elif opcion == '3':
            ver_paciente()
        elif opcion == '4':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()



def menu_enfermero(enfermero):
    while True:
        borrarPantalla()
        print(f"""
        .:: Menú Enfermero ::.
        Bienvenido(a) Enf. {enfermero[1]} {enfermero[2]}
        1.- Registrar Paciente
        2.- Registrar Signos Vitales
        3.- Ver Paciente
        4.- Cerrar Sesión
        """)
        opcion = input("\t Elige una opción: ").upper()
        
        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            registrar_signos_vitales()
        elif opcion == '3':
            ver_paciente()
        elif opcion == '4':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def registrar_diagnostico_y_receta(medico):
    borrarPantalla()
    print("\n \t ..:: Registrar Diagnóstico y Receta ::..")
    id_paciente = input("\t ID del paciente: ")
    diagnostico = input("\t Diagnóstico: ")
    receta = input("\t Receta: ")
    
    if medico.registrar_diagnostico(id_paciente, diagnostico, receta):
        print("\n \t Diagnóstico y receta registrados correctamente.")
    else:
        print("\n \t Error al registrar el diagnóstico y la receta.")
    esperarTecla()

def registrar_signos_vitales():
    borrarPantalla()
    id_paciente = input("ID del paciente: ")
    temperatura = float(input("Temperatura (°C): "))
    presion_sistolica = int(input("Presión sistólica (mm Hg): "))
    presion_diastolica = int(input("Presión diastólica (mm Hg): "))
    pulso = int(input("Pulso (bpm): "))

   
    estado_vitales = enfermero.Enfermero.validar_signos_vitales(
        temperatura, presion_sistolica, presion_diastolica, pulso
    )

    registro_exitoso = enfermero.Enfermero.registrar_signos_vitales(
        id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso
    )

    if registro_exitoso:
        print("Signos vitales registrados exitosamente.")
        print(f"Estado de los signos vitales: {estado_vitales}")
    else:
        print("Error al registrar signos vitales.")
    esperarTecla()


def registrar_paciente():
    borrarPantalla()
    print("\n \t ..:: Registrar Paciente ::..")
    nombre = input("\t Nombre del paciente: ")
    edad = input("\t Edad: ")
    sexo = input("\t Sexo: ")
    tipo_sangre = input("\t Tipo de sangre: ")
    altura = input("\t Altura: ")
    peso = input("\t Peso: ")
    alergias = input("\t Alergias: ")
    numero_cama = input("\t Número de cama: ")
    id_medico = input("\t ID del médico que atendió: ")
    id_enfermero = input("\t ID del enfermero que atendió: ")
    
    paciente_nuevo = paciente.Paciente(nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, id_medico, id_enfermero)
    if paciente_nuevo.registrar():
        print("\n \t Paciente registrado correctamente.")
    else:
        print("\n \t Error al registrar el paciente.")
    esperarTecla()

def ver_paciente():
    borrarPantalla()
    print("\n \t ..:: Ver Paciente ::..")
    id_paciente = input("\t ID del paciente: ")
    paciente_info = paciente.Paciente.obtener(id_paciente)
    signos_vitales = enfermero.Enfermero.obtenerSignos(id_paciente)

    if paciente_info:
        print("\n \t--- Información del Paciente ---")
        print(f"\t Nombre: {paciente_info[1]}")
        print(f"\t Edad: {paciente_info[2]}")
        print(f"\t Sexo: {paciente_info[3]}")
        print(f"\t Tipo de Sangre: {paciente_info[4]}")
        print(f"\t Altura: {paciente_info[5]}")
        print(f"\t Peso: {paciente_info[6]}")
        print(f"\t Alergias: {paciente_info[7]}")
        print(f"\t Número de Cama: {paciente_info[8]}")
        print(f"\t ID Médico atendió: {paciente_info[9]}")
        print(f"\t ID Enfermero que atendió: {paciente_info[10]}")
        print(f"\t Fecha de Registro: {paciente_info[11]}")
    else:
        print("\n \t Paciente no encontrado.")
    
    if signos_vitales:
        print("\n\t--- Signos Vitales ---")
        for signo in signos_vitales:
            print(f"\tTemperatura: {signo[2]}°C")
            print(f"\tPresión Sistólica: {signo[3]} mm Hg")
            print(f"\tPresión Diastólica: {signo[4]} mm Hg")
            print(f"\tPulso: {signo[5]} bpm")
            print(f"\tEstado: {signo[6]}")
    else:
        print("\n \t No se encontraron signos vitales para este paciente.")
    
    esperarTecla()

if __name__ == "__main__":
    menu_principal()
