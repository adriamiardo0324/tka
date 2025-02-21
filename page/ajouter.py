import tkinter as tk
from tkinter import *
from PIL import pillow
root = tk.Tk()
 
root.title("Accueil")
root.geometry("1500x800")





# # Frame ambony
# frame_ambony = tk.Frame(root, bg="lightblue", padx=0, pady=10)
# frame_ambony.place(x=50, y=20, width=300, height=50)
# # Frame accueil
def accueil():
    frame_Accueil = tk.Frame(root, bg="#131199", padx=0, pady=0)
    frame_Accueil.place(x=260, width=1100, height=700)
# frame client
def client():
    frame_client = tk.Frame(root, bg="#1311eb", padx=10, pady=10)
    frame_client.place(x=260, width=1100, height=780)
def reservation():
# frame reservation
    frame_reservation = tk.Frame(root, bg="#2c2beb", padx=10, pady=10)
    frame_reservation.place(x=260, width=1100, height=780)
    
# frame chambre
def chambre():
    frame_chambre = tk.Frame(root, bg="#2c5deb", padx=10, pady=10)
    frame_chambre.place(x=260, width=1100, height=780)
    
# frame de payement
def payement():
    frame_payement = tk.Frame(root, bg="lightpink", padx=10, pady=10)
    frame_payement.place(x=260, width=1100, height=780)
    
# frame Utilisateur
def utilisateur():
    frame_utilisateur = tk.Frame(root, bg="#2c8feb", padx=10, pady=10)
    frame_utilisateur.place(x=260, width=1100, height=780)

# icon1=Image.Open(file="E:\leçon Dayan\GIT projet\icon\home-icon-silhouette.png")
# sary_teraka = Image.open("icon.png")  
# sary_voakely = sary_teraka.Resize((50, 50))
# sary_tk = Image.PhotoImage(sary_voakely)

# Front premier
# Frame ankavia
frame_ankavia = tk.Frame(root,bg="#2c8feb", padx=10, pady=10)
frame_ankavia.place(x=0, y=0, width=250, height=1200)
# label = Label(root, image=sary_tk)
# label.pack(pady=20)
lab1=tk.Button(frame_ankavia, compound="left", text="Accueil & Statistique", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=accueil).place(x=10,y=50)
lab2= tk.Button(frame_ankavia, text="Gestion des clients", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=client).place(x=10,y=100)
lab3=tk.Button(frame_ankavia, text="Gestion des reservations", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=reservation).place(x=10,y=150)
lab4=tk.Button(frame_ankavia, text="gestion des chambres", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=chambre).place(x=10,y=200)
lab5= tk.Button(frame_ankavia, text="Gestion des payement", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=payement).place(x=10,y=250)
lab6=tk.Button(frame_ankavia, text="Utilisateurs", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10),command=utilisateur).place(x=10,y=300)
lab7=tk.Button(frame_ankavia, text="Deconnexion", bg="#2c8feb",fg="white",relief="flat",font=("Arial",10)).place(x=10,y=350)

# fenetre.mainloop()


root.mainloop()