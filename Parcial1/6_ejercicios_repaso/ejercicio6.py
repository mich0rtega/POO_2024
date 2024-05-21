# Mostrar todas la stablas del uno al 10. ostrando el titulo de la tabla y multiplicando dle 1 al 10

tabla = int(input("Ingesa el num para calcular su tabla de multiplicar"))
i = 1
multi = 0
while i <=10:
    multi = i * tabla 
    print(f"{tabla}, x {i} = {multi}")
    i+=1