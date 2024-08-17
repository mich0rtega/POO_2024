from conexionBD import *
import datetime

class Paciente:
    def __init__(self, nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, id_medico, id_enfermero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.tipo_sangre = tipo_sangre
        self.altura = altura
        self.peso = peso
        self.alergias = alergias
        self.numero_cama = numero_cama
        self.id_medico = id_medico
        self.id_enfermero = id_enfermero

    def registrar(self):
        try:
            fecha = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO pacientes VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,NOW())",
                (self.nombre, self.edad, self.sexo, self.tipo_sangre, self.altura, self.peso, self.alergias, self.numero_cama, self.id_medico, self.id_enfermero)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def obtener(id_paciente):
        try:
            cursor.execute(
                "SELECT * FROM pacientes WHERE id = %s", 
                (id_paciente,)
            )
            return cursor.fetchone()
        except:
            return None
        
