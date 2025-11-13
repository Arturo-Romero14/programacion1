import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas
sales_data = {
    "Game ID": ["G1","G2","G3","G4","G5","G6 "],

    "Title": ["Elden Ring", "Dead Space", "Luigi's Mansion" ,"Minecraft", "EAFC 26", "Sekiro"],
    
    "Genre":["RPG","RPG","Horror","Sandbox","Sports","RPG"],
    
    "Publisher":["FromSoftware","EA","Nintendo","Mojang","EA","FromSoftware"],

    "Units_Sold_Millions":[15.5,20,10,67,14,25]
}   

sales_df = pd.DataFrame(sales_data)



#Fuente 2: Reseñas de criticos(externos)
reviews_data = {
    "Game ID": ["G1","G2","G3","G4","G5","G7"],#Nota, G6 falta, G7 sobra.
    "Critic_Score":[7.5,9.5,8.8,7.3,6.1,5.7], #Puntuacion de 0 a 10
    "User_Score":[5.1,9.9,7.8,np.nan,10,6.7] #Un nan! Alguien olvido la calificacion de Minecraft
}

reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de Ventas (Crudos) ---")
print(sales_df)
print("--- Datos de Reseñas (Crudos) ---")
print(reviews_df)

#Limpieza de datos y reparacion
#Desicion: Rellenar l
mean_user_score = reviews_df["User_Score"].mean()#Sacamos el promedio
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpias,NaN rellenado con {mean_user_score}) ---")
print(reviews_df)

#Fusion de tablas(merge)
#Fusionar tabla de ventas con reseñas, Game ID como llave
#INNER JOIN. Nos quedamos con los juegos que existen en ambas tablas
#G6 va a desaparecer, G7 tambien

df = pd.merge(sales_df,reviews_df, on="Game ID", how="inner")

print("\n--- Tabla Fusionada de ventas+reseñas ---")
print(df)


#Crear nuevas columnas que nos den mas información
#Columna estimación de ingresos (asumiendo que vale $50 cada juego)
df