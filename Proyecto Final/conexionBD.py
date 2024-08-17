import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_clinica'
    )
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print(f"Error:{e}")
    print(f"Tipo De Error:{type(e).__name__}")
    print("Ocurrió un error, inténtelo más tarde.")

