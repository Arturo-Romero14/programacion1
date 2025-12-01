import sys
from colorama import Fore, Style, init

# Importamos todas las funciones de util
from util import (
    cargar_datos,
    guardar_datos,
    agregar_juego,
    eliminar_juego,
    OPCIONES_MENU 
)

# Importamos todas las funciones de graficos y reportes
from graficos_reportes import (
    ver_inventario,
    buscar_juego
)

# Empezamos el colorama
init(autoreset=True)

def mostrar_menu():
    """Muestra el menú principal y pide al usuario que quiere hacer."""
    print(f"\n{Style.BRIGHT}{Fore.BLUE}--- SISTEMA DE INVENTARIO DE VIDEOJUEGOS ---{Style.RESET_ALL}")
    
    # Muestra las opciones importadas de util
    for opcion in OPCIONES_MENU:
        print(opcion)
        
    while True:
        try:
            opcion = input(f"{Fore.CYAN}Seleccione una opción (1-5): ")
            if opcion in ('1', '2', '3', '4', '5',):
                return int(opcion)
            else:
                print(f"{Fore.RED}Error: Opción no válida. Ingrese un número del 1 al 5.")
        except ValueError:
            print(f"{Fore.RED}Error: Ingrese un número válido.")

def main():

    """Función principal que dirije todo el programa."""

    catalogo = cargar_datos() 

    while True:
        opcion = mostrar_menu()
        
        
        if opcion == 1:
        
            ver_inventario(catalogo)
        elif opcion == 2:
        
            agregar_juego(catalogo)
        elif opcion == 3:
        
            eliminar_juego(catalogo)
        elif opcion == 4:
        
            buscar_juego(catalogo)
        elif opcion == 5:
            guardar_datos(catalogo)
            print(f"{Fore.LIGHTBLACK_EX} Saliendo del programa. ¡Hasta pronto!")
            sys.exit()
        
        input(f"\n{Fore.YELLOW}Presione Enter para continuar...")


main()