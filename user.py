from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("Utulisateur")
root.geometry("400x300")

label1 = tk.Label(root,text="username:")
label1.place(x=20,y=50)
input1 = tk.Entry(root)
input1.place(x=20,y=80)

label2 = tk.Label(root,text="Mot de passe:")
label2.place(x=20,y=110)
input2 = tk.Entry(root)
input2.place(x=20,y=130)
btn = tk.Button(root,text="Connexion",bg="#333",padx=60)
btn.place(x=20,y=170)
root.mainloop()

