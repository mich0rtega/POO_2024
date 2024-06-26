"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

MEtODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor
a los atributos del objeto al crearlo, es el primer metodo que se ejcuta al crear
el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede
recibir parametros al momento de crear el objeto


Cuando se crea un metodo constructor se utiliza la función init(), para que se
llame automatucamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parametro es una referencia a la instancia actual de la clase y se utiliza 
para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre dself, puedes llamarlo como quieras, pero tiene
que ser el primer parametro de cualquier funcion de la clase. Es decir por regla 
se utiliza en la palabra self pero puede ser llamado con otro nombre por ekjemplo: valor, abc,parametro,etc

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
      self.color=color
      self.marca=marca
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas
    

    #--------------------------------------------------------------
    #El encapuslamiento o visibilidad es importante que a traves de el es
    #posible que python sepa como va a utilizar y manipular los atributos y
    #metodos de la clase

    #Atributo publico 
    atributo_publico = "soy un atributo publico"

    #Atributo privado
    __atributo_privado = "soy un atributo privado"
    #Nota 1. Para utilizar un atributo provado es necesario usarlo dentro de
    #un metodo publico 

    def MetodoPublico(self):
      return self.__atributo_privado
    
    #Metodo privado
    def __MetodoPrivado(self):
      print("Soy un metodo privado")

    #Nota 2. Par utilizar un metodo privado es necesario usarlo dentro de un metodo publico
    def getMetodoPublico(self):
      self.__MetodoPrivado

    #-----------------------------------------------


    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
     self.velocidad+=1

    def frenar(self):
     self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")  

#Fin definir clase

