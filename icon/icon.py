# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# def soumettre_reservation():
#     messagebox.showinfo("Réservation", "Réservation soumise avec succès !")

# # Créer la fenêtre principale
# fenetre = tk.Tk()
# fenetre.title("Bouton Personnalisé en Tkinter")
# fenetre.geometry("400x300")
# fenetre.config(bg="#f0f0f0")

# # Cadre pour le contenu
# frame_reservation = tk.Frame(fenetre, bg="#ffffff", padx=20, pady=20)
# frame_reservation.pack(expand=True, fill="both")

# # Chargement de l'image pour le bouton avec la nouvelle méthode de redimensionnement
# image_btn = Image.open("icon/shield.png")
# image_btn = image_btn.resize((50, 50), Image.Resampling.LANCZOS)  # Utiliser LANCZOS au lieu de ANTIALIAS
# image_btn = ImageTk.PhotoImage(image_btn)

# # Style du bouton personnalisé
# def on_enter(e):
#     button_soumettre['background'] = '#333'
#     button_soumettre['foreground'] = 'white'

# def on_leave(e):
#     button_soumettre['background'] = '#333'
#     button_soumettre['foreground'] = '#00aaff'

# button_soumettre = tk.Button(frame_reservation, 
#                              image=image_btn, 
#                              text="Soumettre", 
#                              compound="left",
#                              font=("Arial", 14, "bold"), 
#                              bg="#333", 
#                              fg="#00aaff", 
#                              bd=0, 
#                              padx=10, 
#                              pady=5, 
#                              cursor="hand2", 
#                              command=soumettre_reservation)

# button_soumettre.grid(row=8, columnspan=2, pady=20)

# # Effet de survol
# button_soumettre.bind("<Enter>", on_enter)
# button_soumettre.bind("<Leave>", on_leave)

# # Pour éviter que l'image soit supprimée par le garbage collector
# button_soumettre.image = image_btn

# # Lancer la boucle principale
# fenetre.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

def soumettre_reservation():
    messagebox.showinfo("Réservation", "Réservation soumise avec succès !")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Bouton Professionnel en Tkinter")
fenetre.geometry("400x300")
fenetre.config(bg="#f0f0f0")

# Fonction pour créer une image de bouton avec un border-radius professionnel
def creer_bouton_arrondi(width, height, radius, color_bg, color_border, shadow=False):
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    if shadow:
        # Ajouter une ombre douce en arrière-plan
        shadow_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_image)
        shadow_draw.rounded_rectangle((5, 5, width, height), radius, fill=(0, 0, 0, 50))
        image.paste(shadow_image, (0, 0), shadow_image)
    
    # Fond arrondi avec bordure
    draw.rounded_rectangle((0, 0, width, height), radius, fill=color_bg, outline=color_border, width=1)
    
    return ImageTk.PhotoImage(image)

# Initialisation de l'image du bouton
image_bouton = creer_bouton_arrondi(200, 50, 25, "#00aaff", "#0077cc", shadow=True)

# Canvas pour afficher le bouton arrondi
canvas = tk.Canvas(fenetre, width=200, height=50, bg="#f0f0f0", bd=0, highlightthickness=0, relief='flat')
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Afficher l'image arrondie sur le Canvas
image_id = canvas.create_image(100, 25, image=image_bouton)

# Ajouter du texte au bouton
text_id = canvas.create_text(100, 25, text="Soumettre", fill="white", font=("Arial", 14, "bold"))

# Effet de survol (hover)
def on_enter(event):
    global image_bouton
    image_bouton = creer_bouton_arrondi(200, 50, 25, "#0077cc", "#005f99", shadow=True)
    canvas.itemconfig(image_id, image=image_bouton)

def on_leave(event):
    global image_bouton
    image_bouton = creer_bouton_arrondi(200, 50, 25, "#00aaff", "#0077cc", shadow=True)
    canvas.itemconfig(image_id, image=image_bouton)

# Fonction pour gérer le clic sur le bouton
def on_bouton_click(event):
    soumettre_reservation()

# Lier les événements au bouton
canvas.bind("<Button-1>", on_bouton_click)
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)

# Pour éviter le garbage collection de l'image
canvas.image = image_bouton

# Lancer la boucle principale
fenetre.mainloop()
