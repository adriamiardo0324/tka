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
    #Creation card1
    tk_nb = tk.Frame(frame_Accueil,bg="#333")
    tk_nb.place(x=40,y=50,width=200,height=90)
    lab= tk.Label(tk_nb, text="Nombre de client",bg="#333",fg="#fff",font=("Arial",12))
    lab.place(x=30,y=10)
    nb = tk.Label(tk_nb,text="Nombre",bg="#333",fg="#FFF",font=("Arial",12))
    nb.place(x=60,y=40)
    #card 2 
    tk_nb1 = tk.Frame(frame_Accueil,bg="#333")
    tk_nb1.place(x=200,y=50,width=200,height=90)
    lab1= tk.Label(tk_nb1, text="Nombre de client",bg="#333",fg="#fff",font=("Arial",12))
    lab1.place(x=30,y=10)
    nb1 = tk.Label(tk_nb1,text="Nombre",bg="#333",fg="#FFF",font=("Arial",12))
    nb1.place(x=60,y=40)
    #Card 3 
    tk_nb2 = tk.Frame(frame_Accueil,bg="#333")
    tk_nb2.place(x=400,y=50,width=200,height=90)
    lab2= tk.Label(tk_nb2, text="Nombre de client",bg="#333",fg="#fff",font=("Arial",12))
    lab2.place(x=30,y=10)
    nb2 = tk.Label(tk_nb2,text="Nombre",bg="#333",fg="#FFF",font=("Arial",12))
    nb2.place(x=60,y=40)
    
    
    
    
    
    
    
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
    # clear_frame()
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
    # clear_frame()
    frame_payement = tk.Frame(root, bg="lightpink", padx=10, pady=10)
    frame_payement.place(x=260, width=1100, height=780)

    # Fonction pour traiter le paiement
    def process_payment():
        try:
            # Récupérer les informations saisies
            client_name = name_entry.get()
            room_number = room_entry.get()
            amount_due = float(amount_entry.get())
            payment_method = payment_method_var.get()

            # Vérifier si les informations sont complètes
            if not client_name or not room_number or not amount_due:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return

            # Simuler le traitement du paiement
            messagebox.showinfo("Paiement effectué", f"Le paiement de {amount_due}Ar pour {client_name} (chambre {room_number}) a été effectué via {payment_method}.")
            
            # Réinitialiser les champs après le paiement
            name_entry.delete(0, tk.END)
            room_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            payment_method_var.set("Carte")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

    # Création des labels et champs de saisie
    tk.Label(frame_payement, text="Nom du client :").grid(row=0, column=10, sticky="e", padx=10, pady=5)
    name_entry = tk.Entry(frame_payement)
    name_entry.grid(row=0, column=11, sticky="e", padx=10, pady=5)

    tk.Label(frame_payement, text="Numéro de chambre :").grid(row=1, column=10, sticky="e", padx=10, pady=5)
    room_entry = tk.Entry(frame_payement)
    room_entry.grid(row=1, column=11, sticky="e", padx=10, pady=5)

    tk.Label(frame_payement, text="Montant dû :").grid(row=2, column=10, sticky="e", padx=10, pady=5)
    amount_entry = tk.Entry(frame_payement)
    amount_entry.grid(row=2, column=11, sticky="e", padx=10, pady=5)

    tk.Label(frame_payement, text="Méthode de paiement :").grid(row=3, column=10, sticky="e", padx=10, pady=5)
    payment_method_var = tk.StringVar(value="Carte")
    payment_methods = ["Carte", "Espèces", "Virement"]
    payment_menu = tk.OptionMenu(frame_payement, payment_method_var, *payment_methods)
    payment_menu.grid(row=3, column=11, sticky="e", padx=10, pady=5)

    # Bouton pour traiter le paiement
    pay_button = tk.Button(frame_payement, text="Effectuer le paiement", command=process_payment)
    pay_button.grid(row=4, column=11, padx=10, pady=5)

    
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