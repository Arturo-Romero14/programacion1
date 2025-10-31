print("\n---------------Analizador De Texto en Python---------------")

texto = input("Por favor introduzca un texto largo para analizar: ").lower()

# Si el usuario deja el texto vacío
if len(texto.strip()) == 0:
    print("\nEl texto ingresado está vacío. No se puede realizar el análisis.")
else:
    # Pedir tres letras
    letras_buscadas = []
    for i in range(3):
        letra = input(f"Ingresa la letra número {i+1}: ").lower()
        letras_buscadas.append(letra[0])  # tomamos solo el primer carácter

    print("\n--- Análisis del Texto ---")

    # 1. Frecuencia de las letras
    conteo_letras = {}
    print("\n1. Frecuencia de las letras:")
    for letra in letras_buscadas:
        cantidad = texto.count(letra)
        conteo_letras[letra] = cantidad
        print(f"   La letra '{letra}' aparece {cantidad} veces.")

    # 2. Cantidad total de palabras
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    print(f"\n2. Cantidad total de palabras: {cantidad_palabras}")

    # 3 y 4. Primera y última letra del texto
    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"\n3. Primera letra del texto: '{primera_letra}'")
    print(f"4. Última letra del texto: '{ultima_letra}'")

    # 5. Texto con palabras en orden inverso
    palabras_invertidas = palabras[::-1]
    texto_invertido = " ".join(palabras_invertidas)
    print(f"\n5. Texto con palabras en orden inverso:\n   -> {texto_invertido}")

    # 6. Comprobación de la palabra "python"
    print("\n6. Indicador si la palabra 'python' está en el texto:")
    if "python" in texto:
        print("   Sí, está la palabra 'python' en el texto.")
    else:
        print("   No, no está la palabra 'python' en el texto.")