def esperarTecla():
    print("\n\t\tOprime cualquier tecla para continuar")
    input()

def borrarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
