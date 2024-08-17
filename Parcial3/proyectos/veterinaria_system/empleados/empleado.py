from conexionBD import *

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def registrarEmp(self):
        try:
            cursor.execute(
                "INSERT INTO empleados VALUES (null, %s, %s, %s)",
                (self.nombre, self.puesto, self.salario)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def actualizarEmp(id, nombre, puesto, salario):
        try:
            cursor.execute(
                "update empleados set nombre=%s, puesto=%s, salario=%s WHERE id=%s",
                (nombre, puesto, salario, id)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminarEmp(id):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE id= %s",
                (id,)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def verEmp(id):
        try:
            cursor.execute(
                "SELECT * FROM empleados WHERE id=%s",
                (id,)
            )
            return cursor.fetchone()  
        except:
            return None