import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class ReserverChambre:
    def __init__(self, root):
        self.root = root
        self.root.title("Enregistrer Chambre")
        self.root.geometry("600x500")
        self.root.configure(bg="#2c8feb")

        # Connexion à la base de données MySQL
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abc123++",
            database="Mania_hotel"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

        title = tk.Label(root, text="ENREGISTRER", font=("Arial", 14, "bold"), bg="#2c8feb", fg="white")
        title.pack(pady=10)

        frame = tk.Frame(root, bg="#2c8feb", bd=5)
        frame.pack(pady=20, padx=40)

        self.create_label_entry(frame, "Name", 0)
        self.create_label_entry(frame, "Address", 1)
        self.create_label_entry(frame, "Contact", 2)
        self.create_label_entry(frame, "Stay Days", 3)

        # Types de chambres
        room_label = tk.Label(frame, text="Type of Room", font=("Arial", 10, "bold"), bg="#2c8feb", fg="white")
        room_label.grid(row=4, column=0, sticky="w", pady=5)

        self.room_vars = {room: tk.IntVar() for room in ["Simple", "Double", "Suite"]}
        for idx, (room, var) in enumerate(self.room_vars.items()):
            tk.Checkbutton(frame, text=room, variable=var, bg="#2c8feb", fg="white").grid(row=4, column=idx + 1, sticky="w")

        # Boutons
        btn_frame = tk.Frame(root, bg="#2c8feb")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Ajouter", font=("Arial", 12, "bold"), bg="#28a745", fg="white", command=self.add_entry).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Modifier", font=("Arial", 12, "bold"), bg="#ffc107", fg="black", command=self.update_entry).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Annuler", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", command=root.quit).pack(side="left", padx=10)

    def create_label_entry(self, frame, text, row):
        label = tk.Label(frame, text=text, font=("Arial", 10, "bold"), bg="#2c8feb", fg="white")
        label.grid(row=row, column=0, sticky="w", pady=5)
        entry = tk.Entry(frame, width=30)
        entry.grid(row=row, column=1, columnspan=2, pady=5)
        setattr(self, f"{text.lower().replace(' ', '_')}_entry", entry)

    def add_entry(self):
        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        contact = self.contact_entry.get().strip()
        stay_days = self.stay_days_entry.get().strip()
        selected_rooms = ", ".join([room for room, var in self.room_vars.items() if var.get()])
        
        if not all([name, address, contact, stay_days, selected_rooms]):
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs")
            return
        
        self.cursor.execute("INSERT INTO reservations (name, address, contact, stay_days, room_type) VALUES (%s, %s, %s, %s, %s)",
                            (name, address, contact, stay_days, selected_rooms))
        self.conn.commit()
        messagebox.showinfo("Succès", "Réservation ajoutée avec succès !")

    def update_entry(self):
        messagebox.showinfo("Modification", "La modification est à implémenter")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReserverChambre(root)
    root.mainloop()