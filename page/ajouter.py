import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
"""from PIL import pillow"""

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

       # Titre
    label_titre = tk.Label(frame_client, text="Gestion des Clients", font=("Arial", 16), bg="#1311eb", fg="white")
    label_titre.pack(pady=10)

    # Labels et champs de saisie
    tk.Label(frame_client, text="Nom :", font=("Arial", 12), bg="#1311eb", fg="white").place(x=50, y=60)
    entry_nom = tk.Entry(frame_client, font=("Arial", 12))
    entry_nom.place(x=200, y=60)

    tk.Label(frame_client, text="Prénom :", font=("Arial", 12), bg="#1311eb", fg="white").place(x=50, y=100)
    entry_prenom = tk.Entry(frame_client, font=("Arial", 12))
    entry_prenom.place(x=200, y=100)

    tk.Label(frame_client, text="Email :", font=("Arial", 12), bg="#1311eb", fg="white").place(x=50, y=140)
    entry_email = tk.Entry(frame_client, font=("Arial", 12))
    entry_email.place(x=200, y=140)

    # Fonctions des boutons
    def ajouter_client():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        email = entry_email.get()

        if nom and prenom and email:
            tree.insert("", "end", values=(nom, prenom, email))
            entry_nom.delete(0, tk.END)
            entry_prenom.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")

    def supprimer_client():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
        else:
            messagebox.showwarning("Suppression", "Veuillez sélectionner un client à supprimer.")

    def modifier_client():
        selected_item = tree.selection()
        if selected_item:
            tree.item(selected_item, values=(entry_nom.get(), entry_prenom.get(), entry_email.get()))
        else:
            messagebox.showwarning("Modification", "Veuillez sélectionner un client à modifier.")

    # Boutons
    btn_ajouter = tk.Button(frame_client, text="Ajouter", font=("Arial", 12), bg="green", fg="white", command=ajouter_client)
    btn_ajouter.place(x=50, y=200)

    btn_modifier = tk.Button(frame_client, text="Modifier", font=("Arial", 12), bg="orange", fg="white", command=modifier_client)
    btn_modifier.place(x=150, y=200)

    btn_supprimer = tk.Button(frame_client, text="Supprimer", font=("Arial", 12), bg="red", fg="white", command=supprimer_client)
    btn_supprimer.place(x=250, y=200)

    # Table pour afficher la liste des clients
    columns = ("Nom", "Prénom", "Email")
    tree = ttk.Treeview(frame_client, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    tree.place(x=50, y=250, width=600, height=400)

    
    
def reservation():
# frame reservation
    frame_reservation = tk.Frame(root, bg="#2c2beb", padx=10, pady=10)
    frame_reservation.place(x=260, width=1100, height=780)
    
# frame chambre
def chambre():
    frame_chambre = tk.Frame(root, bg="#2c5deb", padx=10, pady=10)
    frame_chambre.place(x=260, width=1100, height=780)
    
    def ouvrir_fenetre_liste():
        fenetre = tk.Toplevel(root)
        fenetre.title("Liste des Chambres")
        fenetre.geometry("500x400")
        label = tk.Label(fenetre, text="Liste des chambres", font=("Arial", 14))
        label.pack(pady=20)

        # Table pour afficher les chambres
        columns = ("ID", "Nom", "Type", "Prix")
        tree = ttk.Treeview(fenetre, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        tree.pack(expand=True, fill="both")

    def ouvrir_fenetre_ajout():
        fenetre = tk.Toplevel(root)
        fenetre.title("Ajouter une Chambre")
        fenetre.geometry("400x300")

        tk.Label(fenetre, text="Type:").pack(pady=5)
        entry_type = tk.Entry(fenetre)
        entry_type.pack()

        tk.Label(fenetre, text="Prix:").pack(pady=5)
        entry_prix = tk.Entry(fenetre)
        entry_prix.pack()

        def ajouter():
            messagebox.showinfo("Ajout", "Chambre ajoutée avec succès")
            fenetre.destroy()

        btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter)
        btn_ajouter.pack(pady=10)

    def ouvrir_fenetre_modif():
        fenetre = tk.Toplevel(root)
        fenetre.title("Modifier une Chambre")
        fenetre.geometry("400x300")
        tk.Label(fenetre, text="Modification de Chambre").pack(pady=20)

    def ouvrir_fenetre_suppr():
        fenetre = tk.Toplevel(root)
        fenetre.title("Supprimer une Chambre")
        fenetre.geometry("400x300")
        tk.Label(fenetre, text="Suppression de Chambre").pack(pady=20)

    label_titre = tk.Label(frame_chambre, text="Gestion des Chambres", font=("Arial", 16), bg="blue", fg="white")
    label_titre.pack(pady=20)

    btn_liste = tk.Button(frame_chambre, text="Liste des Chambres", font=("Arial", 12), bg="blue", fg="white",
                            command=ouvrir_fenetre_liste)
    btn_liste.pack(pady=10)

    btn_ajout = tk.Button(frame_chambre, text="Ajouter Chambre", font=("Arial", 12), bg="blue", fg="white",
                            command=ouvrir_fenetre_ajout)
    btn_ajout.pack(pady=10)

    btn_modifier = tk.Button(frame_chambre, text="Modifier Chambre", font=("Arial", 12), bg="blue", fg="white",
                                command=ouvrir_fenetre_modif)
    btn_modifier.pack(pady=10)

    btn_suppr = tk.Button(frame_chambre, text="Supprimer Chambre", font=("Arial", 12), bg="blue", fg="white",
                            command=ouvrir_fenetre_suppr)
    btn_suppr.pack(pady=10) 

# fin frame chambre
    
    
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