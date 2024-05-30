
print("Menu de opciones")
print("1. Suma")
print("2. Resta")
print("3. Multi")
print("4. Divi")
print("5. Salir")

opc = (input("Ingrese el numero de la opc")).upper()
if opc == "5" or opc=="SALIR":
   print("Adios, Terminaste, Gracias por usar mi sistema")
else:
  n1 = int(input("Numero 1:"))
  n2 = int(input("Numero 2:"))


if opc == "1" or opc=="SUMA" or opc=="+":
   print(f"{n1}+{n2}=({n1 + n2}")
elif opc == "2" or opc=="RESTA" or opc=="-":
   print(f"{n1}-{n2}={n1 - n2}")
elif opc == "3" or opc=="MULTI" or opc=="*":
   print(f"{n1}*{n2}={n1 * n2}")
elif opc == "4" or opc=="DIVI" or opc=="/":
   print(f"{n1}/{n2}={n1 / n2}")
