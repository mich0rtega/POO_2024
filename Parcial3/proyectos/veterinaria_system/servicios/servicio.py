from conexionBD import *

class Servicio:
    def __init__(self, tipo, detalle, fecha, cliente_id, animal_id, empleado_id):
        self.tipo = tipo
        self.detalle = detalle
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.animal_id = animal_id
        self.empleado_id = empleado_id

    def registrarServicio(self):
        try:
            query = """
            INSERT INTO servicios VALUES (null, %s, %s, %s, %s, %s, %s)
            """
            params = (self.tipo, self.detalle, self.fecha, self.cliente_id, self.animal_id, self.empleado_id)
            cursor.execute(query, params)
            conexion.commit()
            print("Servicio registrado correctamente.")
            return True
        except Exception as e:
            print(f"Error al registrar servicio: {e}")
            conexion.rollback()
            return False

    @staticmethod
    def verServicio(id_servicio):
        try:
            query = "SELECT * FROM servicios WHERE id_servicio = %s"
            cursor.execute(query, (id_servicio,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener servicio: {e}")
            return None

class Cita:
    def __init__(self, fecha, cliente_id, animal_id, empleado_id, estado):
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.animal_id = animal_id
        self.empleado_id = empleado_id
        self.estado = estado

    def registrarCita(self):
        try:
            query = """
            INSERT INTO citas VALUES (null,%s, %s, %s, %s, %s)
            """
            params = (self.fecha, self.cliente_id, self.animal_id, self.empleado_id, self.estado)
            cursor.execute(query, params)
            conexion.commit()
            print("Cita registrada correctamente.")
            return True
        except Exception as e:
            print(f"Error al registrar cita: {e}")
            conexion.rollback()
            return False

    @staticmethod
    def verCita(id_cita):
        try:
            query = "SELECT * FROM citas WHERE id_cita = %s"
            cursor.execute(query, (id_cita,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener cita: {e}")
            return None

    

class Consulta:
    def __init__(self, motivo, fecha, cliente_id, animal_id, empleado_id):
        self.motivo = motivo
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.animal_id = animal_id
        self.empleado_id = empleado_id

    def registrarConsulta(self):
        try:
            query = """
            INSERT INTO consultas VALUES (null,%s, %s, %s, %s, %s)
            """
            params = (self.motivo, self.fecha, self.cliente_id, self.animal_id, self.empleado_id)
            cursor.execute(query, params)
            conexion.commit()
            print("Consulta registrada correctamente.")
            return True
        except Exception as e:
            print(f"Error al registrar consulta: {e}")
            conexion.rollback()
            return False

    @staticmethod
    def verConsulta(id_consulta):
        try:
            query = "SELECT * FROM consultas WHERE id_consulta = %s"
            cursor.execute(query, (id_consulta,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener consulta: {e}")
            return None

class Vacuna:
    def __init__(self, nombre, fecha_aplicacion, cliente_id, animal_id, empleado_id):
        self.nombre = nombre
        self.fecha_aplicacion = fecha_aplicacion
        self.cliente_id = cliente_id
        self.animal_id = animal_id
        self.empleado_id = empleado_id

    def registrarVacuna(self):
        try:
            query = """
            INSERT INTO vacunas VALUES (null,%s, %s, %s, %s, %s)
            """
            params = (self.nombre, self.fecha_aplicacion, self.cliente_id, self.animal_id, self.empleado_id)
            cursor.execute(query, params)
            conexion.commit()
            print("Vacuna registrada correctamente.")
            return True
        except Exception as e:
            print(f"Error al registrar vacuna: {e}")
            conexion.rollback()
            return False

    @staticmethod
    def verVacuna(id_vacuna):
        try:
            query = "SELECT * FROM vacunas WHERE id_vacuna = %s"
            cursor.execute(query, (id_vacuna,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener vacuna: {e}")
            return None
