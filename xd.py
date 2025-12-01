import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
import sys
import os

# Inicializa colorama para que funcione en terminales de Windows/VS Code
init(autoreset=True)

# 2. Uso de Estructuras de Datos: Tuplas para datos inmutables (ej. menú fijo)
OPCIONES_MENU = (
    f"{Fore.GREEN}1. Ver Inventario y Estadísticas",
    f"{Fore.YELLOW}2. Comprar Juego",
    f"{Fore.LIGHTGREEN_EX}3. Agregar Nuevo Juego",
    f"{Fore.RED}4. Eliminar Juego",
    f"{Fore.MAGENTA}5. Buscar Juego por Nombre",
    f"{Fore.LIGHTBLACK_EX}6. Salir"
)

ARCHIVO_DATOS = 'catalogo_juegos.csv'

# ==============================================================================
# 4. Calidad de Código y Modularidad: Funciones para separar lógicas
# ==============================================================================

def cargar_datos():
    """
    3. Librerías Obligatorias: pandas
    Carga el catálogo de juegos desde un archivo CSV. Si no existe, crea un 
    catálogo inicial (Lista de Diccionarios).
    """
    try:
        # Uso de pandas: Cargar datos desde CSV
        df = pd.read_csv(ARCHIVO_DATOS)
        # Convertir el DataFrame a una lista de diccionarios para la manipulación
        return df.to_dict('records')
    except FileNotFoundError:
        # 2. Uso de Estructuras de Datos: Lista de Diccionarios como catálogo principal
        catalogo_inicial = [
            {
                "nombre": "Zelda", "precio": 90, "inventario": 25,
                "categoria": "Acción / Aventura", "plataformas": "Nintendo Switch",
                "descripcion": "The Legend of Zelda: Tears of the Kingdom."
            },
            {
                "nombre": "God Of War", "precio": 60, "inventario": 8,
                "categoria": "Acción / Hack and Slash", "plataformas": "PlayStation 4 y 5",
                "descripcion": "God of War Ragnarök."
            },
            {
                "nombre": "Halo", "precio": 30, "inventario": 20,
                "categoria": "Shooter / Ciencia Ficción", "plataformas": "Xbox One / Series",
                "descripcion": "Halo Infinite."
            }
        ]
        print(f"{Fore.YELLOW}Aviso: No se encontró '{ARCHIVO_DATOS}'. Se cargó el catálogo inicial.")
        return catalogo_inicial

def guardar_datos(catalogo):
    """
    3. Librerías Obligatorias: pandas
    Guarda el catálogo actual (Lista de Diccionarios) en un archivo CSV.
    """
    # Uso de pandas: Convertir estructura a DataFrame
    df = pd.DataFrame(catalogo)
    # Uso de pandas: Guardar el DataFrame a CSV
    df.to_csv(ARCHIVO_DATOS, index=False)
    print(f"{Fore.GREEN}¡Catálogo guardado exitosamente en '{ARCHIVO_DATOS}'!")

def mostrar_menu():
    """
    Muestra el menú principal y pide la opción al usuario.
    """
    print(f"\n{Style.BRIGHT}{Fore.BLUE}--- SISTEMA DE INVENTARIO DE VIDEOJUEGOS ---{Style.RESET_ALL}")
    # 2. Uso de Estructuras de Datos: Recorrido de Tupla con for
    for opcion in OPCIONES_MENU:
        print(opcion)
        
    while True:
        try:
            opcion = input(f"{Fore.CYAN}Seleccione una opción (1-6): ")
            # 1. Lógica de Control: Condicionales (validación de entrada)
            if opcion in ('1', '2', '3', '4', '5', '6'):
                return int(opcion)
            else:
                print(f"{Fore.RED}Error: Opción no válida. Ingrese un número del 1 al 6.")
        except ValueError:
            print(f"{Fore.RED}Error: Ingrese un número válido.")

def obtener_juego(catalogo, nombre_juego):
    """
    Busca un juego por nombre usando un bucle.
    """
    nombre_juego = nombre_juego.strip().title() # Estandarizar nombre
    # 1. Lógica de Control: Bucles (for para recorrer lista/diccionario)
    for juego in catalogo:
        # Uso de Diccionarios: Búsqueda por llave
        if juego['nombre'] == nombre_juego:
            return juego
    return None

def agregar_juego(catalogo):
    """
    Implementa la funcionalidad para añadir un nuevo juego.
    """
    print(f"\n{Fore.CYAN}--- AGREGAR NUEVO JUEGO ---")
    
    # 1. Lógica de Control: Validación de entradas con bucle while
    while True:
        nombre = input("Nombre del Juego: ").strip().title()
        if obtener_juego(catalogo, nombre):
            print(f"{Fore.RED}Error: El juego '{nombre}' ya existe en el catálogo.")
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
    
    # 2. Uso de Estructuras de Datos: .append() en Listas
    catalogo.append(nuevo_juego)
    print(f"{Fore.GREEN}¡Juego '{nombre}' agregado exitosamente!")

def eliminar_juego(catalogo):
    """
    Implementa la funcionalidad para eliminar un juego.
    """
    print(f"\n{Fore.CYAN}--- ELIMINAR JUEGO ---")
    nombre = input("Ingrese el nombre del juego a eliminar: ").strip().title()
    juego = obtener_juego(catalogo, nombre)

    # 1. Lógica de Control: Condicionales (if/elif/else)
    if juego:
        # 2. Uso de Estructuras de Datos: .remove() / del en Listas
        confirmar = input(f"¿Está seguro que desea eliminar '{nombre}'? (si/no): ").lower()
        if confirmar == 'si':
            catalogo.remove(juego)
            print(f"{Fore.GREEN}Juego '{nombre}' eliminado exitosamente.")
        else:
            print(f"{Fore.YELLOW}Operación cancelada.")
    else:
        print(f"{Fore.RED}Error: El juego '{nombre}' no se encontró en el catálogo.")

def comprar_juego(catalogo):
    """
    Implementa la lógica de compra con validación de existencia.
    """
    print(f"\n{Fore.CYAN}--- COMPRAR JUEGO ---")
    
    # 3. Librerías Obligatorias: pandas - Mostrar datos tabulares
    df_inventario = pd.DataFrame(catalogo)[['nombre', 'precio', 'inventario']]
    print("\n--- Catálogo Disponible ---")
    print(df_inventario.to_string(index=False)) # print(df)
    
    nombre = input("\nIngrese el nombre del juego que desea comprar: ").strip().title()
    juego = obtener_juego(catalogo, nombre)
    
    # 1. Lógica de Control: Condicionales (validación y toma de decisiones)
    if juego:
        print(f"Información: {juego['nombre']} - Precio: ${juego['precio']} - Stock: {juego['inventario']}")
        
        while True:
            try:
                cantidad = int(input("¿Cuántas unidades desea comprar?: "))
                if cantidad <= 0:
                    print(f"{Fore.RED}Error: La cantidad debe ser mayor a cero.")
                elif juego['inventario'] >= cantidad:
                    juego['inventario'] -= cantidad
                    print(f"{Fore.GREEN}¡Compra exitosa! Total: ${juego['precio'] * cantidad}. Quedan {juego['inventario']} unidades de {juego['nombre']}.")
                    break
                else:
                    print(f"{Fore.RED}Error: Solo quedan {juego['inventario']} unidades.")
                break
            except ValueError:
                print(f"{Fore.RED}Error: Ingrese una cantidad numérica válida.")
    else:
        print(f"{Fore.RED}Error: El juego '{nombre}' no se encontró.")

def ver_inventario(catalogo):
    """
    Muestra el catálogo como tabla con pandas y genera gráfica con matplotlib.
    """
    print(f"\n{Fore.CYAN}--- INVENTARIO Y ESTADÍSTICAS ---")
    
    # 3. Librerías Obligatorias: pandas
    # Uso de pandas: Convertir estructura (Lista de Diccionarios) a DataFrame
    df = pd.DataFrame(catalogo)
    
    # Uso de pandas: Mostrar datos ordenados (ordenar por inventario)
    df_ordenado = df.sort_values(by='inventario', ascending=False)
    print("\n--- Inventario Ordenado por Existencias ---")
    print(df_ordenado.to_string(index=False))

    # 3. Librerías Obligatorias: matplotlib
    # Generar gráfica de barras con existencias
    plt.figure(figsize=(10, 6))
    plt.bar(df['nombre'], df['inventario'], color=['blue', 'green', 'red'])
    plt.xlabel("Juegos")
    plt.ylabel("Cantidad en Inventario")
    plt.title("Existencias de Juegos en el Catálogo")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig('inventario_barras.png')
    print(f"\n{Fore.GREEN}Gráfico de inventario generado en 'inventario_barras.png'.")
    # plt.show() # Descomentar para ver el gráfico inmediatamente si no se usa VS Code

def buscar_juego(catalogo):
    """
    Permite buscar un juego y ver toda su información.
    """
    print(f"\n{Fore.CYAN}--- BUSCAR JUEGO ---")
    nombre = input("Ingrese el nombre del juego a buscar: ").strip().title()
    juego = obtener_juego(catalogo, nombre)

    if juego:
        print(f"\n{Style.BRIGHT}{Fore.MAGENTA}--- INFORMACIÓN DETALLADA DE {juego['nombre']} ---")
        for llave, valor in juego.items():
            print(f"{llave.title()}: {valor}")
        print("-" * 40)
    else:
        print(f"{Fore.RED}Error: El juego '{nombre}' no se encontró en el catálogo.")

def main():
    """
    Función principal que ejecuta el menú interactivo.
    1. Lógica de Control: Bucles (while para el menú principal)
    """
    catalogo = cargar_datos()

    while True:
        opcion = mostrar_menu()
        
        # 1. Lógica de Control: Condicionales (match/case sería ideal en Python 3.10+,
        # pero usamos if/elif/else por compatibilidad y simplicidad)
        if opcion == 1:
            ver_inventario(catalogo)
        elif opcion == 2:
            comprar_juego(catalogo)
        elif opcion == 3:
            agregar_juego(catalogo)
        elif opcion == 4:
            eliminar_juego(catalogo)
        elif opcion == 5:
            buscar_juego(catalogo)
        elif opcion == 6:
            guardar_datos(catalogo)
            print(f"{Fore.LIGHTBLACK_EX}Saliendo del programa. ¡Hasta pronto!")
            sys.exit()
        
        input(f"\n{Fore.YELLOW}Presione Enter para continuar...") # Pausa para facilitar la lectura en consola

if __name__ == "__main__":
    main()