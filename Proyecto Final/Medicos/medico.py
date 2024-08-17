from conexionBD import *
import hashlib

class Medico:
    def __init__(self, nombre, apellidos, numEmpleado, password, especialidad, turno):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numEmpleado = numEmpleado
        self.contrasena = self.hash_password(password)
        self.especialidad = especialidad
        self.turno = turno

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            cursor.execute(
                "INSERT INTO medicos (nombre, apellidos, numEmpleado, password, especialidad, turno) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.numEmpleado, self.contrasena, self.especialidad, self.turno)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error en registrar médico: {e}")
            return False

    @staticmethod
    def login(numEmpleado, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "SELECT * FROM medicos WHERE numEmpleado = %s AND password = %s",
                (numEmpleado, contrasena)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Error en login médico: {e}")
            return None

    @staticmethod
    def registrar_diagnostico(id_paciente, diagnostico, receta):
        try:
            cursor.execute(
                "INSERT INTO diagnosticos VALUES (NULL,%s, %s, %s, NOW())",
                (id_paciente, diagnostico, receta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error en registrar diagnóstico: {e}")
            return False

