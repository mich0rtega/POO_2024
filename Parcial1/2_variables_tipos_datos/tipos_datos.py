#Los tipos de datos más comunes en python son:
#primitivos
#int "Entero"
#float "Real"
#str "Cadena"
#bool "logico"

#Estructurados
#list "listas"
#tuple
#dict "como un objeto"


#Ejemplo de Primitivos
entero = 80
real = 3.1416
caracter = '@'
logico = False

#Ejemplo de Estructurados
palabra = "hola"
lista = {10,20,30,40}
lista2 = {"hola", True,'@',30,1.8}

tupla = (
    "Hola", "Como", "estas"
)

diccionario = {
    "nombre": "Daniel",
    "Apellido": "Contreras Ramirez",
    "Especialidad": "TI",
    "Edad": 20
}


#Mostrar los tipos de datos
print (type(entero))
print (type(real))
print (type(caracter))
print (type(logico))

print (type(palabra))
print (type(lista))
print (type(lista2))
print (type(tupla))
print (type(diccionario))
