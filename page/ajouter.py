import tkinter as tk
from tkinter import *
from PIL import pillow
from tkinter import messagebox
from datetime import datetime
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
    
    # Fonction qui sera appelée lors de la soumission de la réservation
    def soumettre_reservation():
        nom = entry_nom.get()
        email = entry_email.get()
        telephone = entry_telephone.get()
        service = service_var.get()
        date_heure = entry_date_heure.get()
        nombre_personnes = entry_nombre_personnes.get()
        paiement = paiement_var.get()
        montant_paye = entry_montant_paye.get()
        
        
    # Vérification des champs obligatoires
        if not nom or not email or not telephone or not date_heure or not nombre_personnes or not montant_paye:
            messagebox.showerror("Erreur", "Tous les champs obligatoires doivent être remplis.")
            return

        try:
            # Vérifier que la date et l'heure sont valides
            datetime.strptime(date_heure, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Erreur", "Le format de la date/heure est incorrect. Utilisez 'AAAA-MM-JJ HH:MM'.")
            return
        
    # Affichage des informations de la réservation dans une boîte de dialogue
        reservation_details = f"""
        Nom: {nom}
        Email: {email}
        Téléphone: {telephone}
        Service: {service}
        Date et Heure: {date_heure}
        Nombre de personnes: {nombre_personnes}
        Mode de paiement: {paiement}
        Montant payé: {montant_paye}
        """
        messagebox.showinfo("Réservation Confirmée", f"Réservation confirmée :\n{reservation_details}")

        
# Création des étiquettes et des champs de texte pour la réservation
    tk.Label(frame_reservation, text="Nom:", bg="#2c2beb", fg="white").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_nom = tk.Entry(frame_reservation, width=30)
    entry_nom.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Email:", bg="#2c2beb", fg="white").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_email = tk.Entry(frame_reservation, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Téléphone:", bg="#2c2beb", fg="white").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_telephone = tk.Entry(frame_reservation, width=30)
    entry_telephone.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Service:", bg="#2c2beb", fg="white").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    service_var = tk.StringVar()
    service_menu = tk.OptionMenu(frame_reservation, service_var, "Hôtel", "Restaurant", "Événement", "Massage")
    service_menu.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Date et Heure (AAAA-MM-JJ HH:MM):", bg="#2c2beb", fg="white").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_date_heure = tk.Entry(frame_reservation, width=30)
    entry_date_heure.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Nombre de personnes:", bg="#2c2beb", fg="white").grid(row=5, column=0, sticky="e", padx=10, pady=5)
    entry_nombre_personnes = tk.Entry(frame_reservation, width=30)
    entry_nombre_personnes.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Mode de paiement:", bg="#2c2beb", fg="white").grid(row=6, column=0, sticky="e", padx=10, pady=5)
    paiement_var = tk.StringVar()
    paiement_menu = tk.OptionMenu(frame_reservation, paiement_var, "Carte de crédit", "Virement", "Espèces")
    paiement_menu.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(frame_reservation, text="Montant payé:", bg="#2c2beb", fg="white").grid(row=7, column=0, sticky="e", padx=10, pady=5)
    entry_montant_paye = tk.Entry(frame_reservation, width=30)
    entry_montant_paye.grid(row=7, column=1, padx=10, pady=5)
    
     # Bouton pour soumettre la réservation
    button_soumettre = tk.Button(frame_reservation, text="Soumettre", command=soumettre_reservation)
    button_soumettre.grid(row=8, columnspan=2, pady=20)
    
# frame chambre
def chambre():
    frame_chambre = tk.Frame(root, bg="#2c5deb", padx=10, pady=10)
    frame_chambre.place(x=260, width=1100, height=780)
    
# frame de payement
def payement():
    frame_payement = tk.Frame(root, bg="lightpink", padx=10, pady=10)
    frame_payement.place(x=260, width=1100, height=780)
    
 # Titre de la section Paiement
    tk.Label(frame_payement, text="Paiement", bg="lightpink", fg="black", font=("Arial", 16)).pack(pady=20)

   
    
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