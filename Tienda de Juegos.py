info_tienda = ("GameStop", "2004")

inventario = { 
    "Elden Ring": {'precio': 60, 'stock': 18},
    "Hollow Knight": {'precio': 15, 'stock': 25}, 
    "Dead Space": {'precio': 25, 'stock': 50} 
}

print ("Los juegos disponibles son:") 
print(inventario)
print("===============================================")

juego = input("Que juego quieres comprar? ")
if juego in inventario:
    if inventario[juego]["stock"] > 0:
        inventario[juego]["stock"] -= 1
        print(f"Compraste {juego} por ${inventario[juego]['precio']}.")
        print(f"Quedan {inventario[juego]['stock']} en stock.")
    else:
        print(" Lo sentimos ese juego no esta disponible.")
else:
    print("Ese juego no lo tenemos disponible")

