from conexionBD import *

# CLIENTES
class Clientes:
    def __init__(self, nombre, telefono, email, direccion):
        self.id_cliente = None  # Inicializar con None
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def registrarClie(self):
        try:
            cursor.execute(
                "INSERT INTO clientes VALUES (null,%s, %s, %s, %s)",
                (self.nombre, self.telefono, self.email, self.direccion)
            )
            conexion.commit()
            self.id_cliente = cursor.lastrowid  # Obtener el último ID insertado
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False

    @staticmethod
    def actualizarClie(id_cliente, nombre, telefono, email, direccion):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre=%s, telefono=%s, email=%s, direccion=%s WHERE id_cliente=%s",
                (nombre, telefono, email, direccion, id_cliente)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    @staticmethod
    def eliminarClie(id_cliente):
        try:
            cursor.execute(
                "DELETE FROM clientes WHERE id_cliente=%s",
                (id_cliente,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False

    @staticmethod
    def verClie(id_cliente):
        try:
            cursor.execute(
                "SELECT * FROM clientes WHERE id_cliente=%s",
                (id_cliente,)
            )
            return cursor.fetchone()  # Solo un resultado esperado
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
            return []

# ANIMAL
class Animal:
    def __init__(self, nombre, raza, edad, cliente_Id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.cliente_Id = cliente_Id

    def registrarAnimal(self):
        try:
            cursor.execute(
                "INSERT INTO animales VALUES (null,%s, %s, %s, %s)",
                (self.nombre, self.raza, self.edad, self.cliente_Id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar animal: {e}")
            return False

    @staticmethod
    def verAnimales(cliente_Id):
        try:
            cursor.execute(
                "SELECT * FROM animales WHERE cliente_Id=%s",
                (cliente_Id,)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener animales: {e}")
            return []
