from colorama import init,Fore,Style 
import random

init()

#Config de colores en el juego

COLORES_POSIBLES = {
    "R": Fore.RED+"◼",
    "N": Fore.BLACK+"◼",
    "V": Fore.GREEN+"◼",
    "A": Fore.BLUE+"◼",
    "Y": Fore.YELLOW+"◼",
    "M": Fore.MAGENTA+"◼",
    "C": Fore.CYAN+"◼",
    "B": Fore.WHITE+"◼"
}

LONGITUD_CODIGO = 5
MAX_INTENTOS = 10

def generar_codigo():
    colores = list(COLORES_POSIBLES.keys())
    codigo_secreto = []
    for _ in range(LONGITUD_CODIGO):
        codigo_secreto.append(random.choice(colores))
    return codigo_secreto


def mostrar_colores_disponibles():
    print("Colores Disponibles:")
    for letra,color_formato in COLORES_POSIBLES.items():
        print(f" {letra}: {color_formato} {Style.RESET_ALL}", end=" ")


def obtener_intento_usuario():
    mostrar_colores_disponibles()
    while True:
        intento = input(f"Ingresa tu codigo de {LONGITUD_CODIGO} letras: \n").upper().strip()

        if len(intento) != LONGITUD_CODIGO:
            print(Fore.RED+f"Error: El código debe tener {LONGITUD_CODIGO} letras"+Style.RESET_ALL)
            continue

        valido = True
        for letra in intento:
            if letra not in COLORES_POSIBLES:
                print(Fore.RED+f"Error: La letra '{letra}' no es un color valido. "+Style.RESET_ALL)
                valido = False
                break
        
        if valido:
            return list(intento)


def evaluar_intento(intento,codigo_secreto):

    posicion_correcta = 0  
    color_correcto = 0

    #Listas para no contar los coloers 2 veces
    intento_copia = list(intento)
    secreto_copia = list(codigo_secreto)


    #Posicion correcta(color verde)
    for i in range(LONGITUD_CODIGO-1,-1,-1):
        if intento_copia[i] == secreto_copia[i]:
            posicion_correcta+=1
            intento_copia.pop(i)
            secreto_copia.pop(i)

    for letra in intento_copia:
        if letra in secreto_copia:
            color_correcto+=1
            secreto_copia.remove(letra)    


    return posicion_correcta,color_correcto

def mostrar_tablero(intentos_pasados,pistas_pasadas):
    """Mostrar el historial de intentos con sus pistas"""
    print("\n--- Tablero del juego ---")
    for i in range(len(intentos_pasados)):
        intento_str=""
        for letra in intentos_pasados[i]:
            intento_str += COLORES_POSIBLES[letra] + Style.RESET_ALL+" "
        
        #Pistas
        pistas_str = (Fore.GREEN
                      + f"{pistas_pasadas[i][0]}P "
                      + Fore.YELLOW
                      + f"{pistas_pasadas[i][1]}C "
                      + Style.RESET_ALL
                      )
        print(f"Intento {i+1}: {intento_str} | {pistas_str}")
        print("-"*20)
        print("\n")

def jugar():
    init(autoreset = True)

    print(Fore.CYAN+Style.BRIGHT+"="*40)
    print(Fore.CYAN+Style.BRIGHT+"BIENVENIDO A MASTERMIND DE COLORES")
    print(Fore.CYAN+Style.BRIGHT+"="*40 + "\n")
    
    codigo_secreto = generar_codigo()

    intentos_restantes = MAX_INTENTOS
    intentos_pasados = []
    pistas_pasadas = []

    while intentos_restantes > 0:
        print(f"Te quedan {Fore.YELLOW + Style.BRIGHT}{intentos_restantes}{Style.RESET_ALL}intentos")

        intento_actual = obtener_intento_usuario()

        pc, cc = evaluar_intento(intento_actual, codigo_secreto)

        mostrar_tablero(intentos_pasados, pistas_pasadas)

        if pc == LONGITUD_CODIGO:
                print(Fore.GREEN + Style.BRIGHT + "Felicidades! Decifraste el codigo secreto!")
                break
        
        intentos_restantes -=1

    if intentos_restantes == 0:
        print(Fore.RED + Style.BRIGHT + "\n! Oh no! Te quedaste sin intentos")
        secreto_str = " ".join(codigo_secreto)
        print(f"El codigo secreto era " + codigo_secreto)


jugar()