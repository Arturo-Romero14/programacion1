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

LONGITUD_CODIGO = 6
MAX_INTENTOS = 12

def generar_codigo():
    colores = list(COLORES_POSIBLES.keys())
    codigo_secreto = []
    for _ in range(LONGITUD_CODIGO):
        codigo_secreto.append(random.choice(colores))
    return codigo_secreto

codigo = generar_codigo()
print(codigo)
codigo2 = generar_codigo()
print(codigo2)
codigo3 = generar_codigo()
print(codigo3)
codigo4 = generar_codigo()
print(codigo4)