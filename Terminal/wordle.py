import random

palabras = ("Mesas","Silla","Libro","Aguas","Perro",
            "Gatos","Calle","Pared","Fuego","Tanto",
            "Cinco","Noche","Playa","Mundo","Clase",
            "Verde","Dedos","Cielo","Bocas","Coche")

while True:
    palabra = palabras[random.randint(0,len(palabras)-1)] #abajo
    wordle = list(palabra) # "a", "b", "a", "j", "o"
    print("""\035[1;37;44m
========================================[Wordle]==========================================================
    Bienvenido ya he elegido la palabra secreta. Tienes 5 intentos para adivinar la palabra
==========================================================================================================\033[0;30;47m""")
    
    for i in range(5):
        intento = input("Ingrese una palabra de 5 letras sin acento.").lower()[:5]
        indice = 0
        resultado = ""
        correctas = 0
        for letra in intento:
            if letra == wordle[indice]:
                correctas += 1
                resultado += "V\033[1;32m"+letra+"\033[0;30m"
            elif letra in wordle:
                resultado += "A\033[1;33m"+letra+"\033[0;30m"
            else:
                resultado += "R\033[1;31m"+letra+"\033[0;30m"
        print(resultado)
        if correctas == 5:
            break
    if correctas == 5:
        print(f"Felicidades, la palabra era \033[1;32m{palabra}\033[0;30m has acertado.")
    else:
        print(f"Lo siento, has fallado. La palabra era \033[1;31m{palabra}\033[0;30m")
    opcion = input("Deseas jugar otra ronda? (Si/No)").lower()
    if opcion == "no":
        break