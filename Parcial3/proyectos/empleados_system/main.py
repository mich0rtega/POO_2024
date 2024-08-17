#Importes
from empleados import empleado
from funciones import *
#Menu principal
def menu_principal():
    while True:
        borrarPantalla()
        print("""
        .::  Menu Principal ::. 
            1.- Registrar Empleado
            2.- Actualizar Empleado
            3.- Eliminar Empleado
            4.- Leer Empleado
            5.- Salir 
        """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1'or opcion == 'REGISTRAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Registrar Empleado ::..")
            nombre = input("\t Nombre del empleado: ")
            puesto = input("\t Puesto: ")
            salario = input("\t Salario: ")
            nuevo_empleado = empleado.Empleado(nombre, puesto, salario)
            if nuevo_empleado.registrar():
                print(f"\n \t {nombre} registrado correctamente.")
            else:
                print(f'\n \t**Error al registrar el empleado, por favor intente de nuevo**...')
            esperarTecla()

        elif opcion == '2' or opcion=='ACTUALIZAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Actualizar Empleado ::..")
            id_empleado = input("\t ID del empleado: ")
            nombre = input("\t Nuevo nombre del empleado: ")
            puesto = input("\t Nuevo puesto: ")
            salario = input("\t Nuevo salario: ")
            empleado_actualizado = empleado.Empleado(nombre, puesto, salario)
            if empleado_actualizado.actualizar(id_empleado):
                print(f"\n \t Empleado {id_empleado} actualizado correctamente.")
            else:
                print(f'\n \t**Error al actualizar el empleado, por favor intente de nuevo**...')
            esperarTecla()

        elif opcion == '3' or opcion=='ELIMINAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Eliminar Empleado ::..")
            id_empleado = input("\t ID del empleado: ")
            if empleado.Empleado.eliminar(id_empleado):
                print(f"\n \t Empleado {id_empleado} eliminado correctamente.")
            else:
                print(f'\n \t**Error al eliminar el empleado, por favor intente de nuevo**...')
            esperarTecla()

        elif opcion == '4' or opcion=='VER EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Ver Empleado ::..")
            id_empleado = input("\t ID del empleado: ")
            empleado_info = empleado.Empleado.ver(id_empleado)
            if empleado_info:
                print("\n \t Información del Empleado:")
                print(f"\t ID: {empleado_info[0]}")
                print(f"\t Nombre: {empleado_info[1]}")
                print(f"\t Puesto: {empleado_info[2]}")
                print(f"\t Salario: {empleado_info[3]}")
            else:
                print("\n \t Empleado no encontrado.")
            esperarTecla()

        elif opcion == '5' or opcion=='SALIR':
            print("\n\t.. ¡Gracias Bye! ...")
            break

        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
