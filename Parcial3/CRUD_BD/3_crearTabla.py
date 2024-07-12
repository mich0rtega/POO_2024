#import conexionBD
from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "create table clientes(id int primary key auto_increment, nombre varchar(60), direccion varchar (120), tel varchar (10))"
    micursor.execute(sql)

except:
    print("Ocurrio un error, intentelo mas tarde ")
else:
    print("se creo la tabla con exito")


