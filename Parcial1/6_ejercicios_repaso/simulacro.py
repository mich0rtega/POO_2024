#crear un programa que permita calcular e imprimir el precio a pagar por un articulo 
#en el precio a pagar se incluye el iva. El programa deberá de funcionar n veces como
#el usuario desee


respuesta = input("¿Desea realizar el proceso? (si/no): ")
while respuesta.lower() == "si":
    articulo = input("Ingrese el artículo: ")
    precio_art = float(input("Ingrese el precio: "))
    iva = precio_art * 0.16
    precio_neto = iva + precio_art
    print(f"A pagar (con IVA): {precio_neto:.2f}")
    respuesta = input("¿Desea realizar el proceso nuevamente? (si/no): ")






