#Concatenar cadeas de caracteres con contenido de variables

nombres="Michelle Carolina Ortega Rubio"
Especialidad="Area de Desarollo SW Multiplataforma"
Carrera="Ingeniero en Gestión y Desarrollo de SW"

#Primer forma d concatenar
print("Mi nombre es:"+nombres+"estoy en la especialidad de:"+Especialidad+"En la carrera de:"+carrera+)

print("/n")

#Segunda forma de concatenar
print("Mi nombre es: ",nombres,"Estoy en la especialidad de: ",Especialidad,"En la carrera de: ",Carrera)
print("/n")

#Tercera forma de concatenar COMUN PYTHON
print (f"Mi nombre es: {nombres} estoy en la especialidad de: {Especialidad},en la carrera de:{Carrera}" format(nombres,Especialidad,Carrera) 

#Cuarta forma
print("Mi nombre es:{}")