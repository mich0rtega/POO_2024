# Importes
from clientes import cliente_animal
from funciones import *
from empleados import empleado
from servicios.servicio import Servicio, Consulta, Vacuna, Cita
from sucursales import sucursal

# M E N U  V E T E R I N A R I A S
def menu_principal():
    while True:
        print("""
            .::  Menu Principal ::.
            1.- Seleccionar Sucursal
            2.- Ver Sucursales
            3.- Registrar Sucursal
            4.- Salir
        """)
        opcion = input("Ingrese la opcion ").upper()
 #SELECCIONAR SUCURSAL       
              
        if opcion == '1' or opcion == 'SELECCIONAR SUCURSAL':
         borrarPantalla()
         print("\n \t ..:: Seleccionar Sucursal ::..")
         id_sucursal = input("\t Ingresa ID de la sucursal: ")
         objid = sucursal.Sucursal.obtener_sucursal(id_sucursal)
         if objid:  # Aquí revisamos si objid no es None o vacío
          menu_sucursal(objid[0])  # Llamamos al menú de la sucursal con el primer elemento de objid
         else:
          print("\n\t ERROR: Sucursal no encontrada. Verifica el ID e intenta nuevamente.")
          esperarTecla()

            
#VER SUCURSAL
        elif opcion == '2' or opcion == 'VER SUCURSALES':
            borrarPantalla()
            print("\n \t ..:: Ver Sucursales ::..")
            sucursal.Sucursal.verSucursales()
            esperarTecla()
#REGISTRAR SUCURSAL
        elif opcion == '3' or opcion == 'REGISTRAR SUCURSAL':
            borrarPantalla()
            print("\n \t ..:: Registrar Sucursal ::..")
            nombre = input(f"\t Nombre de la sucursal: ")
            telefono = input(f"\t Telefono: ")
            direccion = input(f"\t Direccion:")
            regSucu = sucursal.Sucursal(nombre, telefono, direccion)
            if regSucu.registrarSucursal():
                print(f"\n \t {nombre} registrada correctamente.")
            else:
                print(f'\n \t**Error al registrar la sucursal, por favor intente de nuevo**...')
            esperarTecla()
#SALIR 
        elif opcion == '4' or opcion == 'SALIR':
            print("\n\t.. ¡Gracias Bye! ...")
            break
#OPC NO VALIDA
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

# M E N U  S U C U R S A L E S
def menu_sucursal(id_sucursal):
    while True:
        borrarPantalla()
        print(f"""
        .::  Menu de  {id_sucursal} ::.
            1.- Empleados
            2.- Clientes
            3.- Servicios
            4.- Volver al Menu Principal
        """)
        opcion = input("\t Elige una opción: ").upper()
#INGRESE MENU EMPLEADOS
        if opcion == '1' or opcion == 'EMPLEADOS':
            menu_empleados(id_sucursal)
#INGRESE MENU CLIENTES
        elif opcion == '2' or opcion == 'CLIENTES':
            menu_clientes(id_sucursal)
#INGRESE MENU SERVICIOS
        elif opcion == '3' or opcion == 'SERVICIOS':
            menu_servicios(id_sucursal)
#VOLVER AL MENU PRINCIPAL
        elif opcion == '4' or opcion == 'VOLVER AL MENU PRINCIPAL':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

# M E N U  E M P L E A D O S
def menu_empleados(id_sucursal):
    while True:
        borrarPantalla()
        print(f"""
        .::  Menu de Empleados de {id_sucursal} ::.
            1.- Crear Empleado
            2.- Eliminar Empleado
            3.- Actualizar Empleado
            4.- Ver Empleado
            5.- Volver al Menu de Sucursal
        """)
        opcion = input("\t Elige una opción: ").upper()
#REGISTRAR EMPLEADO
        if opcion == '1' or opcion == 'CREAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Registrar Empleado ::..")
            nombre = input("\t Nombre del empleado: ")
            puesto = input("\t Puesto: ")
            salario = input("\t Salario: ")
            regempleado = empleado.Empleado(nombre, puesto, salario)
            crearemp = regempleado.registrarEmp()
            if crearemp:
                print(f"\n \t {nombre} registrado correctamente.")
            else:
                print(f'\n \t**Error al registrar el empleado, por favor intente de nuevo**...')
            esperarTecla()
#ELIMINAR EMPLEADO
        elif opcion == '2' or opcion == 'ELIMINAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Eliminar Empleado ::..")
            id= input("\t ID del empleado: ")
            if empleado.Empleado.eliminarEmp(id):
                print(f"\n \t Empleado {id} eliminado correctamente.")
            else:
                print(f'\n \t**Error al eliminar el empleado, por favor intente de nuevo**...')
            esperarTecla()
#ACTUALIZAR EMPLEADO
        elif opcion == '3' or opcion == 'ACTUALIZAR EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Actualizar Empleado ::..")
            id = input("\t ID del empleado: ")
            nombre = input("\t Nuevo nombre del empleado: ")
            puesto = input("\t Nuevo puesto: ")
            salario = input("\t Nuevo salario: ")
            actualizaremp= empleado.Empleado.actualizarEmp(id,nombre,puesto,salario)
            if actualizaremp:
                print(f"\t Empleado {id} actualizado correctamente.")
            else:
                print(f'\n \t**Error al actualizar el empleado, por favor intente de nuevo**...')
            esperarTecla()
#VER EMPLEADO
        elif opcion == '4' or opcion == 'VER EMPLEADO':
            borrarPantalla()
            print("\n \t ..:: Ver Empleado ::..")
            id= input("\t ID del empleado: ")
            empleado_info = empleado.Empleado.verEmp(id)
            if empleado_info:
                print("\n \t Información del Empleado:")
                print(f"\t ID: {empleado_info[0]}")
                print(f"\t Nombre: {empleado_info[1]}")
                print(f"\t Puesto: {empleado_info[2]}")
                print(f"\t Salario: {empleado_info[3]}")
            else:
                print("\n \t Empleado no encontrado.")
            esperarTecla()
#VOLVER AL MENU ANTERIOR
        elif opcion == '5' or opcion == 'VOLVER AL MENU DE SUCURSAL':
            break
#OPC NO VALIDA
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

# M E N U  C L I E N T E S
def menu_clientes(id_sucursal):
    while True:
        borrarPantalla()
        print(f"""
        .::  Menu de Clientes de {id_sucursal} ::.
            1.- Ingresar Cliente
            2.- Eliminar Cliente
            3.- Actualizar Cliente
            4.- Ver Cliente
            5.- Volver al Menu de Sucursal
        """)
        opcion = input("\t Elige una opción: ").upper()
        # REGISTRAR CLIENTE
        if opcion == '1' or opcion == 'INGRESAR CLIENTE':
            borrarPantalla()
            print("\n \t ..:: Ingresar Cliente ::..")
            nombre = input("\t Nombre del cliente: ")
            telefono = input("\t Teléfono: ")
            email = input("\t Email: ")
            direccion = input("\t Dirección: ")
            regCliente = cliente_animal.Clientes(nombre, telefono, email, direccion)
            if regCliente.registrarClie():
                print(f"\n \t {nombre} registrado correctamente.")
                print("\n \t ..:: Ingresar Animal del Cliente ::..")
                nombre_animal = input("\t Nombre del animal: ")
                raza = input("\t Raza: ")
                edad = input("\t Edad: ")
                nuevo_animal = cliente_animal.Animal(nombre_animal, raza, edad, regCliente.id_cliente)
                if nuevo_animal.registrarAnimal():
                    print(f"\n \t {nombre_animal} registrado correctamente.")
                else:
                    print(f'\n \t**Error al registrar el animal, por favor intente de nuevo**...')
            else:
                print(f'\n \t**Error al registrar el cliente, por favor intente de nuevo**...')
            esperarTecla()
        # ELIMINAR CLIENTE
        elif opcion == '2' or opcion == 'ELIMINAR CLIENTE':
            borrarPantalla()
            print("\n \t ..:: Eliminar Cliente ::..")
            id_cliente = input("\t ID del cliente: ")
            if cliente_animal.Clientes.eliminarClie(id_cliente):
                print(f"\n \t Cliente {id_cliente} eliminado correctamente.")
            else:
                print(f'\n \t**Error al eliminar el cliente, por favor intente de nuevo**...')
            esperarTecla()
        elif opcion == '3' or opcion == 'ACTUALIZAR CLIENTE':
            borrarPantalla()
            print("\n \t ..:: Actualizar Cliente ::..")
            id_cliente = input("\t ID del cliente: ")
            nombre = input("\t Nuevo nombre del cliente: ")
            telefono = input("\t Nuevo teléfono: ")
            email = input("\t Nuevo email: ")
            direccion = input("\t Nueva dirección: ")
            if cliente_animal.Clientes.actualizarClie(id_cliente, nombre, telefono, email, direccion):
                print(f"\t Cliente {id_cliente} actualizado correctamente.")
            else:
                print(f'\n \t**Error al actualizar el cliente, por favor intente de nuevo**...')
            esperarTecla()
        # VER CLIENTE
        elif opcion == '4' or opcion == 'VER CLIENTE':
            borrarPantalla()
            print("\n \t ..:: Ver Cliente ::..")
            id_cliente = input("\t ID del cliente: ")
            cliente_info = cliente_animal.Clientes.verClie(id_cliente)
            if cliente_info:
                print("\n \t Información del Cliente:")
                print(f"\t ID: {cliente_info[0]}")
                print(f"\t Nombre: {cliente_info[1]}")
                print(f"\t Teléfono: {cliente_info[2]}")
                print(f"\t Email: {cliente_info[3]}")
                print(f"\t Dirección: {cliente_info[4]}")
                animales = cliente_animal.Animal.verAnimales(id_cliente)
                if animales:
                    print("\n \t Animales del Cliente:")
                    for animal in animales:
                        print(f"\t ID Animal: {animal[0]}")
                        print(f"\t Nombre Animal: {animal[1]}")
                        print(f"\t Raza: {animal[2]}")
                        print(f"\t Edad: {animal[3]}")
                else:
                    print("\n \t No hay animales registrados para este cliente.")
            else:
                print("\n \t Cliente no encontrado.")
            esperarTecla()
        # VOLVER AL MENU ANTERIOR
        elif opcion == '5' or opcion == 'VOLVER AL MENU DE SUCURSAL':
            break
#OPC NO VALIDA
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

# M E N U  S E R V I C I O S
def menu_servicios(id_sucursal):
    while True:
        borrarPantalla()
        print("""
        .:: Menu de Servicios ::.
            1.- Registrar Servicio
            2.- Ver Servicio
            3.- Registrar Cita
            4.- Ver Cita
            5.- Registrar Consulta
            6.- Ver Consulta
            7.- Registrar Vacuna
            8.- Ver Vacuna
            9.- Volver al Menu Principal
        """)
        opcion = input("\t Elige una opción: ").strip()

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registrar Servicio ::..")
            tipo = input("\t Tipo de servicio: ")
            detalle = input("\t Detalle del servicio: ")
            fecha = input("\t Fecha (YYYY-MM-DD): ")
            cliente_id = input("\t ID del cliente: ")
            animal_id = input("\t ID del animal: ")
            empleado_id = input("\t ID del empleado: ")
            servicio = Servicio(tipo, detalle, fecha, cliente_id, animal_id, empleado_id)
            if servicio.registrarServicio():
                print("\n \t Servicio registrado correctamente.")
            else:
                print("\n \t**Error al registrar el servicio, por favor intente de nuevo**...")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Ver Servicio ::..")
            id_servicio = input("\t ID del servicio: ")
            servicio_info = Servicio.verServicio(id_servicio)
            if servicio_info:
                print("\n \t Información del Servicio:")

                print(f"\t ID: {servicio_info[0]}")
                print(f"\t Tipo: {servicio_info[1]}")
                print(f"\t Detalle: {servicio_info[2]}")
                print(f"\t Fecha: {servicio_info[3]}")
                print(f"\t Cliente ID: {servicio_info[4]}")
                print(f"\t Animal ID: {servicio_info[5]}")
                print(f"\t Empleado ID: {servicio_info[6]}")
            else:
                print("\n \t Servicio no encontrado.")
            esperarTecla()

        elif opcion == '3':
            borrarPantalla()
            print("\n \t ..:: Registrar Cita ::..")
            fecha = input("\t Fecha (YYYY-MM-DD): ")
            cliente_id = input("\t ID del cliente: ")
            animal_id = input("\t ID del animal: ")
            empleado_id = input("\t ID del empleado: ")
            estado = input("\t Estado de la cita: ")
            cita = Cita(fecha, cliente_id, animal_id, empleado_id, estado)
            if cita.registrarCita():
                print("\n \t Cita registrada correctamente.")
            else:
                print("\n \t**Error al registrar la cita, por favor intente de nuevo**...")
            esperarTecla()

        elif opcion == '4':
            borrarPantalla()
            print("\n \t ..:: Ver Cita ::..")
            id_cita = input("\t ID de la cita: ")
            cita_info = Cita.verCita(id_cita)
            if cita_info:
                print("\n \t Información de la Cita:")
                print(f"\t ID: {cita_info[0]}")
                print(f"\t Fecha: {cita_info[1]}")
                print(f"\t Cliente ID: {cita_info[2]}")
                print(f"\t Animal ID: {cita_info[3]}")
                print(f"\t Empleado ID: {cita_info[4]}")
                print(f"\t Estado: {cita_info[5]}")
            else:
                print("\n \t Cita no encontrada.")
            esperarTecla()

        elif opcion == '5':
            borrarPantalla()
            print("\n \t ..:: Registrar Consulta ::..")
            cliente_id = input("\t ID del cliente: ")
            animal_id = input("\t ID del animal: ")
            empleado_id = input("\t ID del empleado: ")
            motivo = input("\t Motivo de la consulta: ")
            fecha = input("\t Fecha (YYYY-MM-DD): ")
            consulta = Consulta(motivo, fecha, cliente_id, animal_id, empleado_id)
            if consulta.registrarConsulta():
                print("\n \t Consulta registrada correctamente.")
            else:
                print("\n \t**Error al registrar la consulta, por favor intente de nuevo**...")
            esperarTecla()

        elif opcion == '6':
            borrarPantalla()
            print("\n \t ..:: Ver Consulta ::..")
            id_consulta = input("\t ID de la consulta: ")
            consulta_info = Consulta.verConsulta(id_consulta)
            if consulta_info:
                print("\n \t Información de la Consulta:")
                print(f"\t ID: {consulta_info[0]}")
                print(f"\t Motivo: {consulta_info[1]}")
                print(f"\t Fecha: {consulta_info[2]}")
                print(f"\t Cliente ID: {consulta_info[3]}")
                print(f"\t Animal ID: {consulta_info[4]}")
                print(f"\t Empleado ID: {consulta_info[5]}")
            else:
                print("\n \t Consulta no encontrada.")
            esperarTecla()

        elif opcion == '7':
            borrarPantalla()
            print("\n \t ..:: Registrar Vacuna ::..")
            nombre = input("\t Nombre de la vacuna: ")
            fecha_aplicacion = input("\t Fecha de aplicación (YYYY-MM-DD): ")
            cliente_id = input("\t ID del cliente: ")
            animal_id = input("\t ID del animal: ")
            empleado_id = input("\t ID del empleado: ")
            vacuna = Vacuna(nombre, fecha_aplicacion, cliente_id, animal_id, empleado_id)
            if vacuna.registrarVacuna():
                print("\n \t Vacuna registrada correctamente.")
            else:
                print("\n \t**Error al registrar la vacuna, por favor intente de nuevo**...")
            esperarTecla()

        elif opcion == '8':
            borrarPantalla()
            print("\n \t ..:: Ver Vacuna ::..")
            id_vacuna = input("\t ID de la vacuna: ")
            vacuna_info = Vacuna.verVacuna(id_vacuna)
            if vacuna_info:
                print("\n \t Información de la Vacuna:")
                print(f"\t ID: {vacuna_info[0]}")
                print(f"\t Nombre: {vacuna_info[1]}")
                print(f"\t Fecha de Aplicación: {vacuna_info[2]}")
                print(f"\t Cliente ID: {vacuna_info[3]}")
                print(f"\t Animal ID: {vacuna_info[4]}")
                print(f"\t Empleado ID: {vacuna_info[5]}")
            else:
                print("\n \t Vacuna no encontrada.")
            esperarTecla()

        elif opcion == '9':
            break

        else:
            print("\n \t Opción no válida, por favor elija una opción del 1 al 9.")
            esperarTecla()

if __name__ == '__main__':
    menu_principal()
