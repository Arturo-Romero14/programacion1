while True:
    JuegoF = input("Ingrese el nombre de su juego favorito: ")
    Juegos = JuegoF
    opcion = input("Desea agregar mas juegos a la lista de favoritos? (Si/No)").lower()
    if opcion == 'si': 
        JuegoF = input("Ingrese el nombre de su juego favorito: ")
        Juegos = JuegoF
    else:
        break