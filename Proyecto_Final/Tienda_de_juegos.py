import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lista con el valor de cada juego
valor = {
    "Zelda": 90,
    "God Of War": 60,
    "Halo": 30
}

#Lista con el inventario de cada juego
inventario = {
    "Zelda": 25,
    "God Of War": 8,
    "Halo": 20
}

#Información adicional de los juegos
info_juegos = {
    "Zelda": {
        "categoria": "Acción / Aventura",
        "plataformas": "Nintendo Switch",
        "descripcion": "The Legend of Zelda es una franquicia de videojuegos de acción y aventuras en la que el joven héroe Link emprende una misión para rescatar a la Princesa Zelda y salvar la tierra de Hyrule del villano Ganon."
    },
    "God Of War": {
        "categoria": "Acción / Hack and Slash",
        "plataformas": "PlayStation 4 y 5",
        "descripcion": "God Of War-(GOW) es una aclamada saga de videojuegos de acción y aventura que sigue la historia de Kratos, un guerrero espartano, en una brutal y épica búsqueda de venganza contra los dioses que lo traicionaron."
    },
    "Halo": {
        "categoria": "Shooter / Ciencia Ficción",
        "plataformas": "Xbox One / Series",
        "descripcion": "Halo es una franquicia de videojuegos de ciencia ficción, principalmente del género de disparos en primera persona (FPS). La trama se centra en una guerra futurista entre la humanidad, liderada por el supersoldado Jefe Maestro, y una alianza teocrática de razas alienígenas conocida como el Covenant."
    }
}

print("Juegos disponibles:")
for juego, precio in valor.items():
    print(f"{juego.title()} cuesta {precio}")

while True:
    accion = input("¿Quieres comprar un juego o ver el inventario? (Comprar/Inventario): ").lower()

    if accion == "inventario":
        print("Inventario de juegos:")
        nombre_de_juegos = []
        cantidad_de_juegos = []

        for juego, cantidad in inventario.items():
            print(f"{juego}: {cantidad}")
            nombre_de_juegos.append(juego)
            cantidad_de_juegos.append(cantidad)

        respuesta = input("¿Desea ver la gráfica por cantidad o por precio? (Cantidad/Precio): ").lower()

        if respuesta == "cantidad":
            plt.figure(figsize=(8, 5))
            plt.bar(nombre_de_juegos, cantidad_de_juegos)
            plt.xlabel("Juegos")
            plt.ylabel("Cantidad")
            plt.title("Inventario por cantidad")
            plt.show()

        elif respuesta == "precio":
            precios = [valor[juego] for juego in nombre_de_juegos]
            plt.figure(figsize=(8, 5))
            plt.bar(nombre_de_juegos, precios)
            plt.xlabel("Juegos")
            plt.ylabel("Precio")
            plt.yticks(np.arange(0, max(precios) + 1, 10))
            plt.title("Inventario por precio")
            plt.show()

        else:
            print("Opción inválida. Escribe 'Cantidad' o 'Precio'.")

    elif accion == "comprar":
        while True:
            print("Juegos disponibles para comprar:")
            for juego, cantidad in inventario.items():
                print(f"{juego}: {cantidad}")

            juego_a_comprar = input("¿Qué juego quieres seleccionar?: ").lower()

            if juego_a_comprar in inventario:
                # Información del Jugo
                print("\nInformación del juego:")
                print("Juego:", juego_a_comprar.title())
                print("Precio:", valor[juego_a_comprar])
                print("Categoría:", info_juegos[juego_a_comprar]["categoria"])
                print("Plataformas:", info_juegos[juego_a_comprar]["plataformas"])
                print("Descripción:", info_juegos[juego_a_comprar]["descripcion"])

                confirmar = input("¿Desea comprar este juego? (Si/No): ").lower()

                if confirmar == "si":
                    if inventario[juego_a_comprar] > 0:
                        inventario[juego_a_comprar] -= 1
                        print(f"Compra realizada. Quedan {inventario[juego_a_comprar]} de {juego_a_comprar}.")
                    else:
                        print("No hay existencias disponibles.")
                else:
                    print("Compra cancelada. Volviendo a la lista.")
                    continue

            else:
                print("Ese juego no está en el inventario.")

            pregunta = input("¿Desea seguir comprando? (Si/No): ").lower()
            if pregunta == "no":
                print("Gracias por su compra.")
                break

    else:
        print("Opción no válida. Elija 'Comprar' o 'Inventario'.")