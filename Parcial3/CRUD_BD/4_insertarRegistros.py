from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "INSERT INTO clientes(id, nombre, direccion, tel) VALUES (NULL, 'Juan Polainas', 'col.del valle', '6181234567')"
    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalize el sql con exito
    conexion.commit()


except:
    print("Ocurrio un error, intentelo mas tarde ")
else:
    print("Registro insertado con exito")