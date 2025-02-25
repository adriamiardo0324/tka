import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root=tk.Tk()
root.geometry("500x400")
root.title("MANIA HOTEL")


def se_connecter():
    utilisateur = username.get()
    mot_de_passe = password.get()

image = Image.open("/home/tanjona/Documents/mania_hotel/logo.png")
image_tk = ImageTk.PhotoImage(image)
label_image = tk.Label(root,image=image_tk)
label_image.pack()

frame = tk.Frame(root)
frame.pack(expand=True,pady=5)

tk.Label(frame,text="usename:",font="Arial").pack(padx=10)
username = tk.Entry(frame,width=30)
username.pack(padx=10,pady=5)

tk.Label(frame,text="password:",font="Arial").pack(padx=10)
password = tk.Entry(frame,width=30,show="*")
password.pack(padx=10,pady=5)


connexion = tk.Button(root,text="Se connecter",command=se_connecter,font="Arial",width=24,bg="#2c8feb",fg="white")
connexion.pack()




root.mainloop()

