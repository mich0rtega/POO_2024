import os #Es una libreria
from varias_funciobes import * #Importe de funciones desde otro archivo


# def espereTecla():
#         print("Oprime cualquier tecla para continuar")
#         input()
# def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 2:"))

# def calculadora(n1,n2,opcion):

#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
#         return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
#         return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
#         return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
#         return f"{n1}/{n2}={n1/n2}"
    
   

# os.system("cls") #Funcion para limpiar pantalla
# opcion=True
# while opcion:
#     os.system("cls")
#     print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
#     opcion=input("\t Elige una opción: ").upper()
#     if opcion != '5':
#      n1,n2=solicitarNumeros()
#      print(calculadora(n1,n2,opcion))
#      espereTecla()
#     else:
#       opcion=False
#       print("Gracias por utilizar el sistema ...") 
            
