import mysql.connector

try:
    # Conexión con la BD de Mysql
 conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
 )
except Exception as e:
   print(f"Error:{e}")
   print(f"Tipo De Error:{type(e).__name__}")
   print("Ocurrio un error, intentelo mas tarde ")


