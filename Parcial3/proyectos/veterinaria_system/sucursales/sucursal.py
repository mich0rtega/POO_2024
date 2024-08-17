from conexionBD import *


class Sucursal:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def registrarSucursal(self):
        try:
            cursor.execute(
                "INSERT INTO sucursales VALUES (null,%s, %s, %s)",
                (self.nombre, self.telefono, self.direccion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar sucursal: {e}")
            return False

    @staticmethod
    def verSucursales():
        try:
            cursor.execute("SELECT * FROM sucursales")
            sucursales = cursor.fetchall()
            for sucursal in sucursales:
                print(f"ID: {sucursal[0]}, Nombre: {sucursal[1]}, Teléfono: {sucursal[2]}, Dirección: {sucursal[3]}")
        except Exception as e:
            print(f"Error al obtener las sucursales: {e}")

    @staticmethod
    def obtener_sucursal(id_sucursal):
        sucursales = {
            "1": ["Sucursal 1", "Dirección 1"],
            "2": ["Sucursal 2", "Dirección 2"]
        }
        return sucursales.get(id_sucursal)
