#Solicitar 2 numeros al usuario y realizar todas las operaciones basicas de una calculadora
# (+,-,*,/) y mostrar en pantalla el resultado
print("1: suma, 2: resta, 3: multiplicacion, 4: division")
menu = input("Ingrese funcion a realizar: ")


num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))
if menu == "1":
    suma = num1 + num2
    print(f"La suma es: {suma}")
elif menu == "2":
    resta = num1 - num2
    print(f"La resta es: {resta}")
elif menu == "3":
    multi = num1 * num2
    print(f"La multiplicacion es: {multi}")
elif menu == "4":
    division = num1 / num2
    print(f"La multiplicacion es: {division}")



