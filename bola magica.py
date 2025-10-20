import random

def obtener_respuesta():
    respuestas = [
        "Si, definitivamente si."
        "Es decididamente así.",
        "Sin duda.",
        "Pregunta de nuevo más tarde.",
        "Es mejor no decirte ahora.",
        "No puedo predecir ahora.",
        "No cuentes con ello.",
        "Mi respuesta es no.",
        "Mis fuentes dicen que no.",
        "Perspectiva buena.",
        "Muy dudoso."
    ]
    return respuestas

def simular_bola_magica():

    print("\n ¡Bienvenido a la Bola Mágica!")

    opciones = obtener_respuesta()

    while True:
        pregunta = input(("Ingrese una pregunta. Si desea salir escribe 'salir'.")).lower()
       
        if not pregunta.strip():
            continue
        respuesta_elegida = random.choice(opciones)
        print(f"\nLa Bola Mágica dice: {respuesta_elegida}\n")
        if pregunta == 'salir':
            print("Siempre sera bienvenido...")
            break

simular_bola_magica()