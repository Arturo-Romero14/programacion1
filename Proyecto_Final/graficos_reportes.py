import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
from util import obtener_juego

def ver_inventario(catalogo):
    """
    Mostramos el catálogo como tabla usando pandas y generamos la gráfica usando matplotlib.

    """
    print(f"\n{Fore.CYAN}--- INVENTARIO Y ESTADÍSTICAS ---")
    
    # Convertimos la Lista de Diccionarios a un DataFrame.
    df = pd.DataFrame(catalogo)
    
    # Mostramos los datos ordenados.
    df_ordenado = df.sort_values(by='inventario', ascending=False)
    print("\n--- Inventario Ordenado por Existencias ---")
    print(df_ordenado.to_string(index=False))

    # Mostramos la grafica.
    plt.figure(figsize=(10, 6))
    plt.bar(df['nombre'], df['inventario'], color=['blue', 'green', 'red'])
    plt.xlabel("Juegos")
    plt.ylabel("Cantidad en Inventario")
    plt.title("Existencias de Juegos en el Catálogo")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig('inventario_barras.png')
    print(f"\n{Fore.GREEN}Gráfico de inventario generado en 'inventario_barras.png'.")
    # plt.show() # Lo comente para ver si funcionaba el savefig y si lo hace. :)

def buscar_juego(catalogo):
    """
    Esta funcion nos permite buscar un juego y ver toda su información.

    """
    print(f"\n{Fore.CYAN}--- BUSCAR JUEGO ---")
    nombre = input("Ingrese el nombre del juego a buscar: ").lower()
    juego = obtener_juego(catalogo, nombre)

    if juego:
        print(f"\n{Style.BRIGHT}{Fore.MAGENTA}--- INFORMACIÓN DETALLADA DE {juego['nombre']} ---")
        for llave, valor in juego.items():
            print(f"{llave.title()}: {valor}")
        print("-" * 40)
    else:
        print(f"{Fore.RED}Error: El juego '{nombre}' no se encontró en el catálogo.")