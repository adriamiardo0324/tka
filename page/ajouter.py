import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from datetime import datetime
from tkcalendar import DateEntry
from PIL import Image, ImageTk

"""from PIL import pillow"""

root = tk.Tk()
root.title("Accueil")
root.geometry("1500x800")


def ouvrir_connexion():
    # Fonction qui ouvre la page de connexion
    global frame_connexion
    frame_connexion = tk.Frame(root, bg="#f4f4f4", padx=10, pady=10)
    frame_connexion.place(x=0, y=0, width=500, height=400)

    label_username = tk.Label(frame_connexion, text="Nom d'utilisateur :")
    label_username.pack(pady=10)
    entry_username = tk.Entry(frame_connexion)
    entry_username.pack(pady=5)

    label_password = tk.Label(frame_connexion, text="Mot de passe :")
    label_password.pack(pady=10)
    entry_password = tk.Entry(frame_connexion, show="*")
    entry_password.pack(pady=5)

    def connecter():
        # Vérification des informations de connexion
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "admin":  # Exemple de validation
            frame_connexion.destroy()  # Fermer la page de connexion
            ouvrir_page_principale()  # Ouvrir la page principale
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    bouton_connexion = tk.Button(frame_connexion, text="Se connecter", command=connecter)
    bouton_connexion.pack(pady=20)

# # Frame ambony
# frame_ambony = tk.Frame(root, bg="lightblue", padx=0, pady=10)
# frame_ambony.place(x=50, y=20, width=300, height=50)
# # Frame accueil
import mysql.connector

def accueil():
    frame_Accueil = tk.Frame(root, bg="#131199", padx=20, pady=20)
    frame_Accueil.place(x=260, width=1100, height=700)

    # Connexion à la base de données
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_db"
        )
        cursor = conn.cursor()

        # Récupération des données du nombre de clients et d'occupation
        cursor.execute("SELECT SUM(nombre_occupe) FROM chambres")
        chambres_occupees = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(nombre_total) FROM chambres")
        chambres_disponibles = cursor.fetchone()[0] or 0

        total_clients = chambres_occupees
        taux_occupation = round((chambres_occupees / chambres_disponibles) * 100, 2) if chambres_disponibles > 0 else 0

        # Récupération des types de chambres
        cursor.execute("SELECT type, nombre_occupe FROM chambres")
        types_chambres = cursor.fetchall()

        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur de connexion", f"Impossible de se connecter à la base de données : {err}")
        return

    # 🎨 Style des cartes
    card_bg = "#333"
    card_fg = "#fff"
    card_font = ("Arial", 14, "bold")

    # 📌 Fonction pour créer une carte d'information
    def create_card(parent, text, value, x, y):
        card = tk.Frame(parent, bg=card_bg, bd=2, relief="ridge")
        card.place(x=x, y=y, width=250, height=100)

        tk.Label(card, text=text, bg=card_bg, fg=card_fg, font=card_font).pack(pady=10)
        tk.Label(card, text=str(value), bg=card_bg, fg="#FFD700", font=("Arial", 16, "bold")).pack()

    # 🏨 Affichage des cartes (statistiques principales)
    create_card(frame_Accueil, "Nombre de Clients", total_clients, 40, 50)
    create_card(frame_Accueil, "Taux d'Occupation (%)", f"{taux_occupation}%", 310, 50)
    create_card(frame_Accueil, "Chambres Disponibles", chambres_disponibles, 580, 50)

    # 📊 Tableau du classement des types de chambres
    tk.Label(frame_Accueil, text="Classement des Types de Chambres", bg="#131199", fg="white",
             font=("Arial", 14, "bold")).place(x=40, y=200)

    # Création du tableau
    columns = ("Type de Chambre", "Nombre Réservé")
    tree = ttk.Treeview(frame_Accueil, columns=columns, show="headings", height=6)
    tree.place(x=40, y=230, width=500, height=200)

    # Définition des colonnes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=200)

    # Remplissage des données depuis la base
    for chambre, nombre in types_chambres:
        tree.insert("", "end", values=(chambre, nombre))
    
 
# Connexion à la base de données MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Problème de connexion à la base de données : {err}")
        return None

# Interface Client
def client():
    frame_client = tk.Frame(root, bg="#1311eb", padx=10, pady=10)
    frame_client.place(x=260, width=1100, height=780)

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

    # Table pour afficher la liste des clients
    columns = ("ID", "Nom", "Prénom", "Email")
    tree = ttk.Treeview(frame_client, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    tree.place(x=50, y=250, width=800, height=400)

    # Charger les clients depuis la base
    def charger_clients():
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients")
            rows = cursor.fetchall()
            tree.delete(*tree.get_children())  # Effacer l'ancienne liste
            for row in rows:
                tree.insert("", "end", values=row)
            conn.close()

    # Ajouter un client
    def ajouter_client():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        email = entry_email.get()

        if nom and prenom and email:
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO clients (nom, prenom, email) VALUES (%s, %s, %s)", (nom, prenom, email))
                    conn.commit()
                    messagebox.showinfo("Succès", "Client ajouté avec succès !")
                    charger_clients()
                except mysql.connector.Error as err:
                    messagebox.showerror("Erreur", f"Problème d'insertion : {err}")
                conn.close()
        else:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")

    # Supprimer un client
    def supprimer_client():
        selected_item = tree.selection()
        if selected_item:
            client_id = tree.item(selected_item, "values")[0]
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM clients WHERE id = %s", (client_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Suppression", "Client supprimé avec succès.")
                charger_clients()
        else:
            messagebox.showwarning("Suppression", "Veuillez sélectionner un client à supprimer.")

    # Modifier un client
    def modifier_client():
        selected_item = tree.selection()
        if selected_item:
            client_id = tree.item(selected_item, "values")[0]
            nom = entry_nom.get()
            prenom = entry_prenom.get()
            email = entry_email.get()

            if nom and prenom and email:
                conn = connect_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE clients SET nom = %s, prenom = %s, email = %s WHERE id = %s",
                                   (nom, prenom, email, client_id))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Modification", "Client modifié avec succès.")
                    charger_clients()
            else:
                messagebox.showwarning("Modification", "Veuillez remplir tous les champs.")
        else:
            messagebox.showwarning("Modification", "Veuillez sélectionner un client à modifier.")

    # Boutons
    btn_ajouter = tk.Button(frame_client, text="Ajouter", font=("Arial", 12), bg="green", fg="white", command=ajouter_client)
    btn_ajouter.place(x=50, y=200)

    btn_modifier = tk.Button(frame_client, text="Modifier", font=("Arial", 12), bg="orange", fg="white", command=modifier_client)
    btn_modifier.place(x=150, y=200)

    btn_supprimer = tk.Button(frame_client, text="Supprimer", font=("Arial", 12), bg="red", fg="white", command=supprimer_client)
    btn_supprimer.place(x=250, y=200)

    # Charger les données au démarrage
    charger_clients()
    
# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="hotel_db"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Erreur", f"Erreur de connexion à la base de données : {err}")

def reservation():
    frame_reservation = tk.Frame(root, bg="#f4f4f4", bd=2, relief="ridge")
    frame_reservation.place(x=260, width=1100, height=780)

    def soumettre_reservation():
        nom = entry_nom.get()
        email = entry_email.get()
        telephone = entry_telephone.get()
        service = service_var.get()
        date_selectionnee = entry_date.get()
        heure_selectionnee = entry_heure.get()
        nombre_personnes = entry_nombre_personnes.get()
        paiement = paiement_var.get()
        montant_paye = entry_montant_paye.get()

        # Fusionner la date sy l'heure
        date_heure = f"{date_selectionnee} {heure_selectionnee}"

        if not nom or not email or not telephone or not date_heure or not nombre_personnes or not montant_paye:
            messagebox.showerror("Erreur", "Tous les champs obligatoires doivent être remplis.")
            return

        try:
            datetime.strptime(date_heure, "%Y-%m-%d %H:%M")  # Vérification du format
        except ValueError:
            messagebox.showerror("Erreur", "Format de la date incorrect. Utilisez 'AAAA-MM-JJ HH:MM'.")
            return

        try:
            cursor.execute("SELECT id FROM clients WHERE email = %s", (email,))
            client = cursor.fetchone()
            if client:
                client_id = client[0]
            else:
                cursor.execute("INSERT INTO clients (nom, email) VALUES (%s, %s)", (nom, email))
                conn.commit()
                client_id = cursor.lastrowid 

            cursor.execute("""
                INSERT INTO reservations (nom, service, date_heure, nombre_personnes, mode_paiement, montant_paye)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nom, service, date_heure, nombre_personnes, paiement, montant_paye))
            conn.commit()

            messagebox.showinfo("Succès", "Réservation enregistrée avec succès !")
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {err}")

    label_style = {"bg": "#f4f4f4", "fg": "#333", "font": ("Arial", 12, "bold")}
    entry_style = {"font": ("Arial", 12), "bd": 2, "relief": "solid", "width": 35}

    tk.Label(frame_reservation, text="Formulaire de Réservation", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white", pady=10).grid(row=0, column=1, sticky="new")

    fields = [
        ("Nom :", entry_style),
        ("Email :", entry_style),
        ("Téléphone :", entry_style),
        ("Nombre de personnes :", entry_style),
        ("Montant payé :", entry_style),
    ]

    entries = []
    for i, (label, style) in enumerate(fields, start=1):
        tk.Label(frame_reservation, text=label, **label_style).grid(row=i, column=0, sticky="e", padx=20, pady=10)
        entry = tk.Entry(frame_reservation, **style)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    entry_nom, entry_email, entry_telephone, entry_nombre_personnes, entry_montant_paye = entries

    # Widget DateEntry ho an'ny daty
    tk.Label(frame_reservation, text="Date :", **label_style).grid(row=6, column=0, sticky="e", padx=20, pady=10)
    entry_date = DateEntry(frame_reservation, width=32, font=("Arial", 12), background='darkblue', foreground='white', date_pattern='yyyy-MM-dd')
    entry_date.grid(row=6, column=1, padx=10, pady=10)

    # Widget Entry ho an'ny heure
    tk.Label(frame_reservation, text="Heure (HH:MM) :", **label_style).grid(row=7, column=0, sticky="e", padx=20, pady=10)
    entry_heure = tk.Entry(frame_reservation, **entry_style)
    entry_heure.grid(row=7, column=1, padx=10, pady=10)

    tk.Label(frame_reservation, text="Service :", **label_style).grid(row=8, column=0, sticky="e", padx=20, pady=10)
    service_var = tk.StringVar()
    service_menu = tk.OptionMenu(frame_reservation, service_var, "Hôtel", "Restaurant", "Événement", "Massage")
    service_menu.config(font=("Arial", 12), width=30, bg="white")
    service_menu.grid(row=8, column=1, padx=10, pady=10)

    tk.Label(frame_reservation, text="Mode de paiement :", **label_style).grid(row=9, column=0, sticky="e", padx=20, pady=10)
    paiement_var = tk.StringVar()
    paiement_menu = tk.OptionMenu(frame_reservation, paiement_var, "Carte de crédit", "Virement", "Espèces")
    paiement_menu.config(font=("Arial", 12), width=30, bg="white")
    paiement_menu.grid(row=9, column=1, padx=10, pady=10)

    button_soumettre = tk.Button(
        frame_reservation, text="Confirmer la réservation", command=soumettre_reservation,
        bg="#27ae60", fg="white", font=("Arial", 14, "bold"), relief="raised", bd=3, padx=10, pady=5
    )
    button_soumettre.grid(row=10, columnspan=2, pady=30)

 
# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",   # Serveur MySQL, ici 'localhost'
        user="root",        # Utilisateur MySQL
        password="",        # Mot de passe MySQL
        database="hotel_db" # Nom de la base de données
    )
    cursor = conn.cursor()
    print("Connexion à la base de données réussie.")
except mysql.connector.Error as err:
    messagebox.showerror("Erreur", f"Erreur de connexion à la base de données : {err}")
    # frame chambre
def chambre():
    frame_chambre = tk.Frame(root, bg="#2c5deb", padx=10, pady=10)
    frame_chambre.place(x=260, width=1100, height=780)
    
    # Liste des chambres
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

        # Récupérer les chambres depuis la base de données
        cursor.execute("SELECT id, nom, type, prix FROM chambre")
        chambres = cursor.fetchall()
        for chambre in chambres:
            tree.insert("", "end", values=chambre)

    # Ajouter une chambre
    def ouvrir_fenetre_ajout():
        fenetre = tk.Toplevel(root)
        fenetre.title("Ajouter une Chambre")
        fenetre.geometry("400x300")

        tk.Label(fenetre, text="Nom:").pack(pady=5)
        entry_nom = tk.Entry(fenetre)
        entry_nom.pack()

        tk.Label(fenetre, text="Type:").pack(pady=5)
        entry_type = tk.Entry(fenetre)
        entry_type.pack()

        tk.Label(fenetre, text="Prix:").pack(pady=5)
        entry_prix = tk.Entry(fenetre)
        entry_prix.pack()

        def ajouter():
            nom = entry_nom.get()
            type_chambre = entry_type.get()
            prix = entry_prix.get()

            if not nom or not type_chambre or not prix:
                messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
                return

            try:
                prix = float(prix)  # Convertir en float pour le prix
            except ValueError:
                messagebox.showerror("Erreur", "Le prix doit être un nombre.")
                return

            # Insérer la chambre dans la base de données
            cursor.execute("INSERT INTO chambre (nom, type, prix) VALUES (%s, %s, %s)", (nom, type_chambre, prix))
            conn.commit()

            messagebox.showinfo("Ajout", "Chambre ajoutée avec succès")
            fenetre.destroy()

        btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter)
        btn_ajouter.pack(pady=10)

    # Modifier une chambre
    def ouvrir_fenetre_modif():
        fenetre = tk.Toplevel(root)
        fenetre.title("Modifier une Chambre")
        fenetre.geometry("400x300")

        tk.Label(fenetre, text="ID de la chambre à modifier:").pack(pady=5)
        entry_id = tk.Entry(fenetre)
        entry_id.pack()

        def modifier():
            chambre_id = entry_id.get()
            if not chambre_id:
                messagebox.showerror("Erreur", "L'ID de la chambre est obligatoire.")
                return

            cursor.execute("SELECT * FROM chambre WHERE id = %s", (chambre_id,))
            chambre = cursor.fetchone()

            if not chambre:
                messagebox.showerror("Erreur", "Chambre non trouvée.")
                return

            # Afficher les champs actuels de la chambre pour modification
            new_nom = messagebox.askstring("Nom", "Entrez le nouveau nom:", initialvalue=chambre[1])
            new_type = messagebox.askstring("Type", "Entrez le nouveau type:", initialvalue=chambre[2])
            new_prix = messagebox.askfloat("Prix", "Entrez le nouveau prix:", initialvalue=chambre[3])

            cursor.execute("""
                UPDATE chambre 
                SET nom = %s, type = %s, prix = %s 
                WHERE id = %s
            """, (new_nom, new_type, new_prix, chambre_id))

            conn.commit()
            messagebox.showinfo("Modification", "Chambre modifiée avec succès")
            fenetre.destroy()

        btn_modifier = tk.Button(fenetre, text="Modifier", command=modifier)
        btn_modifier.pack(pady=10)

    # Supprimer une chambre
    def ouvrir_fenetre_suppr():
        fenetre = tk.Toplevel(root)
        fenetre.title("Supprimer une Chambre")
        fenetre.geometry("400x300")
        tk.Label(fenetre, text="ID de la chambre à supprimer:").pack(pady=5)
        entry_id = tk.Entry(fenetre)
        entry_id.pack()

        def supprimer():
            chambre_id = entry_id.get()
            if not chambre_id:
                messagebox.showerror("Erreur", "L'ID de la chambre est obligatoire.")
                return

            cursor.execute("SELECT * FROM chambre WHERE id = %s", (chambre_id,))
            chambre = cursor.fetchone()

            if not chambre:
                messagebox.showerror("Erreur", "Chambre non trouvée.")
                return

            cursor.execute("DELETE FROM chambres WHERE id = %s", (chambre_id,))
            conn.commit()

            messagebox.showinfo("Suppression", "Chambre supprimée avec succès")
            fenetre.destroy()

        btn_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer)
        btn_supprimer.pack(pady=10)

    # Interface principale
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

# Appel de la fonction chambre pour afficher l'interface
chambre()
    
def payement():
    # Création du frame principal avec un design moderne
    frame_payement = tk.Frame(root, bg="#f8f9fa", padx=20, pady=20, relief="ridge", bd=2)
    frame_payement.place(x=260, width=1100, height=780)

    # Fonction pour traiter le paiement
    def process_payment():
        try:
            # Récupérer les informations saisies
            client_name = name_entry.get().strip()
            room_number = room_entry.get().strip()
            amount_due = amount_entry.get().strip()
            payment_method = payment_method_var.get()

            # Vérifier si les informations sont complètes
            if not client_name or not room_number or not amount_due:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return
            
            # Vérification du montant
            try:
                amount_due = float(amount_due)
                if amount_due <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")
                return

            # Simuler le traitement du paiement
            messagebox.showinfo("Paiement effectué", f"Le paiement de {amount_due} Ar pour {client_name} (chambre {room_number}) a été effectué via {payment_method}.")

            # Réinitialiser les champs après le paiement
            name_entry.delete(0, tk.END)
            room_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            payment_method_var.set("Carte")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

    # Style des labels et entrées
    label_style = {"bg": "#f8f9fa", "fg": "#343a40", "font": ("Arial", 12, "bold")}
    entry_style = {"font": ("Arial", 12), "bd": 2, "relief": "solid", "width": 30}

    # Titre
    tk.Label(frame_payement, text="Paiement de la Réservation", font=("Arial", 16, "bold"), bg="#007bff", fg="white", pady=10).grid(row=0, column=1, sticky="wne")

    # Champs du formulaire
    fields = [
        ("Nom du client :", entry_style),
        ("Numéro de chambre :", entry_style),
        ("Montant dû :", entry_style),
    ]

    entries = []
    for i, (label, style) in enumerate(fields, start=1):
        tk.Label(frame_payement, text=label, **label_style).grid(row=i, column=0, sticky="e", padx=20, pady=10)
        entry = tk.Entry(frame_payement, **style)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    name_entry, room_entry, amount_entry = entries

    # Sélection du mode de paiement
    tk.Label(frame_payement, text="Méthode de paiement :", **label_style).grid(row=4, column=0, sticky="e", padx=20, pady=10)
    payment_method_var = tk.StringVar(value="Carte")
    payment_methods = ["Carte", "Espèces", "Virement"]
    payment_menu = tk.OptionMenu(frame_payement, payment_method_var, *payment_methods)
    payment_menu.config(font=("Arial", 12), width=28, bg="white")
    payment_menu.grid(row=4, column=1, padx=10, pady=10)

    # Bouton pour traiter le paiement
    pay_button = tk.Button(
        frame_payement, text="Effectuer le paiement", command=process_payment,
        bg="#28a745", fg="white", font=("Arial", 14, "bold"), relief="raised", bd=3, padx=10, pady=5
    )
    pay_button.grid(row=5, columnspan=2, pady=30)
    
def utilisateur():
    # Création du frame principal
    frame_utilisateur = tk.Frame(root, bg="#2c8feb", padx=20, pady=20, relief="ridge", bd=2)
    frame_utilisateur.place(x=260, width=1100, height=780)

    # Fonction pour enregistrer l'utilisateur
    def enregistrer_utilisateur():
        nom = entry_nom.get().strip()
        email = entry_email.get().strip()
        role = role_var.get()

        if not nom or not email:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        messagebox.showinfo("Succès", f"L'utilisateur {nom} a été enregistré avec succès en tant que {role}.")
        entry_nom.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        role_var.set("Utilisateur")

    # Style des labels et entrées
    label_style = {"bg": "#2c8feb", "fg": "white", "font": ("Arial", 12, "bold")}
    entry_style = {"font": ("Arial", 12), "bd": 2, "relief": "solid", "width": 30}

    # Titre
    tk.Label(frame_utilisateur, text="Gestion des Utilisateurs", font=("Arial", 16, "bold"), bg="#003366", fg="white", pady=10).grid(row=0, columnspan=2, sticky="we", pady=10)

    # Champs du formulaire
    tk.Label(frame_utilisateur, text="Nom :", **label_style).grid(row=1, column=0, sticky="e", padx=20, pady=10)
    entry_nom = tk.Entry(frame_utilisateur, **entry_style)
    entry_nom.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame_utilisateur, text="Email :", **label_style).grid(row=2, column=0, sticky="e", padx=20, pady=10)
    entry_email = tk.Entry(frame_utilisateur, **entry_style)
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    # Sélection du rôle
    tk.Label(frame_utilisateur, text="Rôle :", **label_style).grid(row=3, column=0, sticky="e", padx=20, pady=10)
    role_var = tk.StringVar(value="Gerant")
    role_options = ["Gerant", "receptionniste"]
    role_menu = tk.OptionMenu(frame_utilisateur, role_var, *role_options)
    role_menu.config(font=("Arial", 12), width=28, bg="white")
    role_menu.grid(row=3, column=1, padx=10, pady=10)

    # Boutons
    btn_enregistrer = tk.Button(frame_utilisateur, text="Enregistrer", command=enregistrer_utilisateur,
                                bg="#28a745", fg="white", font=("Arial", 14, "bold"), relief="raised", bd=3, padx=10, pady=5)
    btn_enregistrer.grid(row=4, column=1, pady=20, sticky="w")

    btn_annuler = tk.Button(frame_utilisateur, text="Annuler", command=lambda: [entry_nom.delete(0, tk.END), entry_email.delete(0, tk.END), role_var.set("Utilisateur")],
                            bg="#dc3545", fg="white", font=("Arial", 14, "bold"), relief="raised", bd=3, padx=10, pady=5)
    btn_annuler.grid(row=4, column=1, pady=20, sticky="e")
# icon1=Image.Open(file="E:\leçon Dayan\GIT projet\icon\home-icon-silhouette.png")
# sary_teraka = Image.open("icon.png")  
# sary_voakely = sary_teraka.Resize((50, 50))
# sary_tk = Image.PhotoImage(sary_voakely)

# Front premier
# Chargement des icônes pour chaque bouton
def charger_icone(icon, size=(20, 20)):
    image = Image.open(icon)
    # image = image.resize(size, Image.ANTIALIAS)
    image = image.resize(size, Image.Resampling.LANCZOS)  
    return ImageTk.PhotoImage(image)

# Définir le frame à gauche
frame_ankavia = tk.Frame(root, bg="#2c8feb", padx=10, pady=10)
frame_ankavia.place(x=0, y=0, width=250, height=1200)

# Charger les icônes pour chaque bouton
icon_accueil = charger_icone("icon/home-icon-silhouette.png")
icon_client = charger_icone("icon/groupe.png")
icon_reservation = charger_icone("icon/shield.png")
icon_chambre = charger_icone("icon/single-bed.png")
icon_payement = charger_icone("icon/credit-card.png")
icon_utilisateur = charger_icone("icon/user.png")
icon_deconnexion = charger_icone("icon/se-deconnecter.png")

# Ajouter les boutons avec icônes
lab1 = tk.Button(frame_ankavia, compound="left", text=" Accueil & Statistique", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_accueil, command=accueil)
lab1.place(x=10, y=50)

lab2 = tk.Button(frame_ankavia, text=" Gestion des clients", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_client, compound="left", command=client)
lab2.place(x=10, y=100)

lab3 = tk.Button(frame_ankavia, text=" Gestion des réservations", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_reservation, compound="left", command=reservation)
lab3.place(x=10, y=150)

lab4 = tk.Button(frame_ankavia, text=" Gestion des chambres", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_chambre, compound="left", command=chambre)
lab4.place(x=10, y=200)

lab5 = tk.Button(frame_ankavia, text=" Gestion des paiements", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_payement, compound="left", command=payement)
lab5.place(x=10, y=250)

lab6 = tk.Button(frame_ankavia, text=" Utilisateurs", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_utilisateur, compound="left", command=utilisateur)
lab6.place(x=10, y=300)
 
def deconnexion():
    # Fonction pour revenir à la page de connexion
    frame_ankavia.destroy()  # Ferme la page principale
    frame_ankavia.destroy()  # Ferme la page principale
    ouvrir_connexion()  # Ouvre la page de connexion

lab7 = tk.Button(frame_ankavia, text=" Déconnexion", bg="#2c8feb", fg="white", relief="flat", font=("Arial", 10), image=icon_deconnexion, compound="left",command=deconnexion)
lab7.place(x=10, y=350)
# fenetre.mainloop()


root.mainloop()