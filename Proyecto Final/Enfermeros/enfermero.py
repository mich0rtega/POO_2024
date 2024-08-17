from conexionBD import *
import hashlib

class Enfermero:
    def __init__(self, nombre, apellidos, numEmpleado, password, area, turno):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numEmpleado = numEmpleado
        self.contrasena = self.hash_password(password)
        self.area = area
        self.turno = turno

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            cursor.execute(
                "INSERT INTO enfermeros VALUES (NULL, %s, %s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.numEmpleado, self.contrasena, self.area, self.turno)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def login(numEmpleado, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "SELECT * FROM enfermeros WHERE numEmpleado = %s AND password = %s",
                (numEmpleado, contrasena)
            )
            return cursor.fetchone()
        except:
            return None

    @staticmethod
    def registrar_signos_vitales(id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso):
    # Determinar el estado de los signos vitales
     estado = Enfermero.validar_signos_vitales(temperatura, presion_sistolica, presion_diastolica, pulso)

     try:
        # Insertar los datos en la tabla
        cursor.execute(
            "INSERT INTO signos_vitales (id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso, estado, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, NOW())",
            (id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso, estado)
        )
        conexion.commit()
        return True
     except Exception as e:
        print(f"Error en registrar signos vitales: {e}")
        return False

     
    @staticmethod
    def validar_signos_vitales(temperatura, presion_sistolica, presion_diastolica, pulso):
     es_normal = True
     
     if not (36.0 <= float(temperatura) <= 37.2):
        es_normal = False
     if not (90 <= int(presion_sistolica) <= 120):
        es_normal = False
     if not (70 <= int(presion_diastolica) <= 80):
        es_normal = False
     if not (66 <= int(pulso) <= 100):
        es_normal = False

     return "Normal" if es_normal else "Anormal"

    
    @staticmethod
    def obtenerSignos(id_paciente):
        cursor.execute("SELECT * FROM signos_vitales WHERE id_paciente = %s", (id_paciente,))
        return cursor.fetchall()

