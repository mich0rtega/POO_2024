""" 
   Comentario de varias lineas
   Nota: a la hora de concatenar cadenas no es posible incluir en algunas ocasiones contenido de variables que no sean de tipo str

"""

#Concatenar un str con str
texto = "Soy una cadema de texto"
print(texto+"soy otra cadena de texto")


#Concatenar un int a str
numero = 23
numero_str = str(numero)
#misma forma de convertir
print("el numero:"+numero_str)
print("el numero:"+str(numero))

#Comcatenar un str a int

n1= '23'
n2= 33

#ES MEJOR HACER EL CAMBIO DENTRO DE LAS EXPRESIONES
suma = int(n1) + n2
print("El numero:"+str(suma))


#Comcatenar un Float y Int a str

n1= '23'
n2= 33.0

suma = int(n1) + n2
print("El numero:"+str(int(suma)))
print(f"el numero:"(int(suma)))

#Comcatenar un Float y float a float
n1= '23.34'
n2= '33.99'

suma = float(n1) + n2
print(f"el numero:"(int(suma)))
