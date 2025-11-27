import tkinter as tk
from tkinter import font
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana
from util.util_imagenes import leer_imagen

def bind_over_events(button):
    button.bind("<Enter>", lambda evento:on_enter(evento,button))
    button.bind("<Leave>", lambda evento:on_leave(evento,button))

def on_enter(evento, button):
    button.config(bg="#0099CC")

def on_leave(evento, button):
    button.config(bg=COLOR_MENU_LATERAL)

def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")

def limpiar_panel():
    for widget in panel.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal)

def mostrar_ventanas():
    limpiar_panel(panel_principal)
    label_ventas = tk.Label(panel_principal,text="Ventas")
    label_ventas.pack()

def cargar_cancion():
    ruta = filedialog.askopenfile(title="Elige un mp3",
                                  filetypes=[("Archivos MP3","*.mp3")])
    if ruta:
        return (ruta,os.path.basename(ruta))

def reproducir(ruta, estado):
    if ruta:
        try:
            if estado == "pause":
                #Si estaba pausado, le quitamos el pause
                pygame.mixer.music.unpause()
                estado = "play"
            else:
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error",
                                 f"No se pudo reproducir el archivo")
    else:
        messagebox.showwarning("Atencion",
                               "Primero debes cargar una cancion")

def pausar():
    pygame.mixer.music.stop()
    return "stop"

def cambiar_volumen

root = tk.Tk()
root.title(TITULO)
icon = tk.PhotoImage(file="./imagenes/sales.png")#No se redimensiona
root.iconphoto(False,icon)
#Geometry
centrar_ventana(root,1024,600)

barra_superior = tk.Frame(root,height=50
                          ,bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral = tk.Frame(root,width=150,bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT,fill="both",expand=False)

panel_principal = tk.Frame(root,width=150
                           ,bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT ,fill="both",expand=True)


#fuentes_disponibles = list(font.families())
#fa_fonts = [f for f in fuentes_disponibles if "Awesome" in f]
#print(fa_fonts)
fontawesome = font.Font(family="Font Awesome 7 Free",size=20)

btn_menu= tk.Button(barra_superior, text="\uf0c9",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=toggle_panel
)

btn_menu.pack(padx=10,pady=10,side=tk.LEFT)

label = tk.Label(barra_superior,text="Programacion I"
                 ,font="Roboto 24"
                 , bg=COLOR_BARRA_SUPERIOR
                 , fg="#f2f2f2"
                 )
label.pack(padx=10,pady=10,side=tk.LEFT)


btn_stop= tk.Button(barra_superior, text="\uf04d",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)


btn_play= tk.Button(barra_superior, text="\uf04b",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)

btn_pause= tk.Button(barra_superior, text="\uf04c",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)

volumen = tk.Scale(barra_superior, from_=0, to=100
                   , bg=COLOR_BARRA_SUPERIOR
                   ,fg="#f2f2f2", bd=0,border=0
                   , resolution=1,orient="horizontal")
volumen.pack(padx=4,pady=10, side=tk.RIGHT)
btn_pause.pack(padx=4,pady=10,side=tk.RIGHT)
btn_play.pack(padx=4,pady=10,side=tk.RIGHT)
btn_stop.pack(padx=4,pady=10,side=tk.RIGHT)

imagen_perfil = leer_imagen("./imagenes/profile.png",(100,100))
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL
                        ,image=imagen_perfil)
label_perfil.pack(side=tk.TOP,pady=20)

btn_inicio = tk.Button(
    menu_lateral, text="Inicio",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_inicio.pack(side=tk.TOP)

btn_productos = tk.Button(
    menu_lateral, text="Productos",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_productos.pack(side=tk.TOP)

btn_ventas = tk.Button(
    menu_lateral, text="Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_ventas.pack(side=tk.TOP)

btn_usuarios = tk.Button(
    menu_lateral, text="Usuarios",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_usuarios.pack(side=tk.TOP)

btn_reportes = tk.Button(
    menu_lateral, text="Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_reportes.pack(side=tk.TOP)

btn_salir = tk.Button(
    menu_lateral, text="Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=10, font="Roboto 20"
)

btn_salir.pack(side=tk.BOTTOM)

bind_over_events(btn_inicio)
bind_over_events(btn_ventas)
bind_over_events(btn_productos)
bind_over_events(btn_usuarios)
bind_over_events(btn_reportes)
bind_over_events(btn_salir)

root.mainloop()

