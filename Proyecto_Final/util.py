import pandas as pd
from colorama import Fore, Style
import os

# Tupla donde mantenemos las opciones que vera el usuario.
ARCHIVO_DATOS = 'catalogo_juegos.csv'
OPCIONES_MENU = (
    f"{Fore.GREEN}1. Ver Inventario y Estadísticas",
    f"{Fore.LIGHTGREEN_EX}2. Agregar Nuevo Juego",
    f"{Fore.RED}3. Eliminar Juego",
    f"{Fore.MAGENTA}4. Buscar Juego por Nombre",
    f"{Fore.LIGHTBLACK_EX}5. Salir"
)

def cargar_datos():
    """Carga el catálogo desde CSV o genera el inicial."""
    try:
        df = pd.read_csv(ARCHIVO_DATOS)
        return df.to_dict('records')
    except FileNotFoundError:
        catalogo_inicial = [
            # Pusimos una lista incial que puede ser modificada.
            {
                "nombre": "The Legend of Zelda: Tears of the Kingdom", "precio": 90, "inventario": 2500,
                "categoria": "Acción / Aventura", "plataformas": "Nintendo Switch",
                "descripcion": "Secuela del juego que revoluciono la saga de zelda."
            },
            {
                "nombre": "God of War Ragnarök", "precio": 60, "inventario": 8000,
                "categoria": "Acción / Hack and Slash", "plataformas": "PlayStation 4 y 5",
                "descripcion": "Secuela del grandioso God Of War del 2018"
            },
            {
                "nombre": "Halo Infinite", "precio": 30, "inventario": 2000,
                "categoria": "Shooter / Ciencia Ficción", "plataformas": "Xbox One / Series",
                "descripcion": "Juego cargado de accion para todas las edades."
            }
        ]
        print(f"{Fore.YELLOW}Aviso: No se encontró '{ARCHIVO_DATOS}'. Se cargó el catálogo inicial.")
        return catalogo_inicial

def guardar_datos(catalogo):
    """Guarda el catálogo actual en un archivo CSV Usando pandas."""
    df = pd.DataFrame(catalogo)
    df.to_csv(ARCHIVO_DATOS, index=False)
    print(f"{Fore.GREEN}¡Catálogo guardado exitosamente en '{ARCHIVO_DATOS}'!")

def obtener_juego(catalogo, nombre_juego):
    """Busca un juego por nombre."""
    nombre_juego = nombre_juego.lower().strip()
    for juego in catalogo:
        if juego['nombre'].strip().lower() == nombre_juego:
            return juego
    return None

def agregar_juego(catalogo):
    """Agrega un nuevo juego."""
    print(f"\n{Fore.LIGHTGREEN_EX}--- AGREGAR NUEVO JUEGO ---")
    
    while True:
        nombre = input("Nombre del Juego: ").strip().title()
        if obtener_juego(catalogo, nombre):
            print(f"{Fore.RED}Error: El juego '{nombre}' ya existe.")
        elif not nombre:
            print(f"{Fore.RED}Error: El nombre no puede estar vacío.")
        else:
            break
            
    while True:
        try:
            precio = float(input("Precio (USD): "))
            inventario = int(input("Cantidad en Inventario: "))
            if precio <= 0 or inventario < 0:
                print(f"{Fore.RED}Error: Precio debe ser positivo y Inventario no negativo.")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}Error: Ingrese un valor numérico válido.")

    categoria = input("Categoría: ").strip().title()
    plataformas = input("Plataformas: ").strip().title()
    descripcion = input("Descripción: ").strip()

    nuevo_juego = {
        "nombre": nombre, "precio": precio, "inventario": inventario,
        "categoria": categoria, "plataformas": plataformas, "descripcion": descripcion
    }
    
    catalogo.append(nuevo_juego)
    print(f"{Fore.GREEN}¡Juego '{nombre}' agregado exitosamente!")

def eliminar_juego(catalogo):
    """Elimina un juego."""
    print(f"\n{Fore.LIGHTRED_EX}--- ELIMINAR JUEGO ---")
    nombre = input("Ingrese el nombre del juego a eliminar: ").strip().title()
    juego = obtener_juego(catalogo, nombre)

    if juego:
        confirmar = input(f"¿Está seguro que desea eliminar '{nombre}'? (si/no): ").lower()
        if confirmar == 'si':
            catalogo.remove(juego)
            print(f"{Fore.GREEN}Juego '{nombre}' eliminado exitosamente.")
        else:
            print(f"{Fore.YELLOW}Operación cancelada.")
    else:
        print(f"{Fore.RED}Error: El juego '{nombre}' no se encontró en el catálogo.")