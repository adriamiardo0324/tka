import tkinter as tk
import ajouter
def go_home():
    ajouter.accueil(root)

def go_about():
    print("À propos")

def go_contact():
    print("Contact")

root = tk.Tk()
root.geometry("600x400")
root.title("Navbar en Tkinter")

# Création de la barre de navigation
navbar = tk.Frame(root, bg="blue", height=10)
navbar.pack(fill="y")

# Ajout des boutons dans la navbar
btn_home = tk.Button(navbar, text="Accueil", command=go_home, fg="white", bg="blue", relief="flat")
btn_home.pack(side="top", padx=0, pady=5)

btn_about = tk.Button(navbar, text="À propos", command=go_about, fg="white", bg="blue", relief="flat")
btn_about.pack(side="top", padx=0, pady=5)

btn_contact = tk.Button(navbar, text="Contact", command=go_contact, fg="white", bg="blue", relief="flat")
btn_contact.pack(side="top", padx=0, pady=5)

root.mainloop()
