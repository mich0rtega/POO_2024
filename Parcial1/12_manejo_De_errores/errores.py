#Menjo de errores es la forma en la que tienen los lenguajes de programación
#Para evitar que sucedan errores en tiempo de ejecucion

#Ejemplo 1 Error cuando una variable no se genera

# try:
#     nombre = input("Dame el nombre")

#     if len(nombre)>1:
#       nombre_usuario = "El nombre es: "+nombre

#     print(nombre_usuario)  
# except:
#     print("Es necesario intruducior un nombre de usuario")

#Ejemplo 2 Cuando se solicita un numero y se introduce una letra

#El else(excepcion) de la excepcion se ejecuta solo si no hay errores en el try

#VALUE ERROR - VALOR INVALIDO 

# try: 
#     numero = int(input("Dame un numero"))

#     if numero >0:
#       print("Soy un numero entero positivo")
#     else:
#       print("Soy un numero entero negativo")
# except:
#    print("No se puede convertir un caracter no numerico a numerico")
# else:
#    print("Todo se ejecuto sin errores ")

#Ejemplo 3 cuando se generan multiplies excepciones
try:
   numero = int(input("Dame un numero: "))
   print("El cuadrado es:" +str(numero * numero))
except ValueError:
   print("Debes de introducir un numero, no se puede convertir un caracter que no sea numerico")
except TypeError:
   print("No es posible convertir el numero a entero")
else:
   print("Finalizo correctamente")
finally:
   print("Listo, se termino")
