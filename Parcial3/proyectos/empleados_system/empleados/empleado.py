from conexionBD import *

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def registrar(self):
        try:
            cursor.execute(
                "INSERT INTO empleados VALUES (null,%s, %s, %s)",
                (self.nombre, self.puesto, self.salario)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar empleado: {e}")
            return False

    def actualizar(self, id_empleado):
        try:
            cursor.execute(
                "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id_empleado = %s",
                (self.nombre, self.puesto, self.salario, id_empleado)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False

    @staticmethod
    def eliminar(id_empleado):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE id_empleado = %s", (id_empleado,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False

    @staticmethod
    def ver(id_empleado):
        try:
            cursor.execute(
                "SELECT * FROM empleados WHERE id_empleado = %s", (id_empleado,)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener empleado: {e}")
            return None

   
