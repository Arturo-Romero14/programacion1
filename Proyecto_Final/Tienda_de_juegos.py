import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista con el valor de cada juego
valor = {
    "zelda": 90,
    "god of war": 60,
    "halo": 30
}

# Lista con el inventario de cada juego
inventario = {
    "zelda": 25,
    "god of war": 8,
    "halo": 20
}

print("Juegos disponibles:")
print("Zelda cuesta", valor["zelda"])
print("God of War cuesta", valor["god of war"])
print("Halo cuesta", valor["halo"])

# Preguntar que desea hacer al cliente
accion = input("¿Quieres comprar un juego o ver el inventario?: ").lower()
if accion == "inventario":
    print("Inventario de juegos:")
    nombre_de_juegos = []
    cantidad_de_juegos = []
    for juego_nombre, cantidad in inventario.items():
        print(f"{juego_nombre}: {cantidad}")
        nombre_de_juegos.append(juego_nombre)
        cantidad_de_juegos.append(cantidad)

    respuesta = input("Desea ver la grafica del inventario por cantidad de juegos o por precio?(Cantidad/Precio): ").lower()
    if respuesta == "cantidad":
        plt.figure(figsize=(8, 5))
        plt.bar(nombre_de_juegos, cantidad_de_juegos, color='skyblue')
        plt.xlabel("Juegos")
        plt.ylabel("Cantidad")
        plt.title("Inventario de juegos por cantidad")
        plt.show()
    elif respuesta == "precio":
        precios_de_juegos = [valor[game] for game in nombre_de_juegos]
        plt.figure(figsize=(8, 5))
        plt.bar(nombre_de_juegos, precios_de_juegos, color='lightgreen')
        plt.xlabel("Juegos")
        plt.ylabel("Precio")
        plt.yticks(np.arange(0, max(precios_de_juegos) + 1, 10))
        plt.title("Inventario de juegos por precio")
        plt.show()
    else:
        print("Error: Elige 'Cantidad' o 'Precio'.")

elif accion == "comprar":
    print("Juegos disponibles para comprar:")
    for juego_nombre_inventario, cantidad in inventario.items():
        print(f"{juego_nombre_inventario}: {cantidad}")

    # Preguntar el juego que se desea comprar
    juego_a_comprar = input("¿Qué juego quieres comprar?: ").lower()
    if juego_a_comprar in valor:
        if inventario[juego_a_comprar] > 0:
            print("¡Gracias por tu compra!")
            inventario[juego_a_comprar] -= 1
            print(f"Quedan {inventario[juego_a_comprar]} juegos de {juego_a_comprar} en el inventario.")
        else:
            print(f"Lo sentimos, no hay {juego_a_comprar} disponibles en este momento.")
    else:
        print(f"Lo sentimos, el juego {juego_a_comprar} no está en el inventario.")
else:
    print("Opción no válida. Por favor, elige 'Comprar' o 'Inventario'.")
