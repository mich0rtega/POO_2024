from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "update clientes set direccion='Col. del UTD' where id=1"
    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalize el sql con exito
    conexion.commit()


except:
    print("Ocurrio un error, intentelo mas tarde ")
else:
    print("Registro Actualizado con exito")