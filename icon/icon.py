from tkinter import *

fenetre = Tk()
fenetre.title("Sary amin'ny Widgets")

# Mampiasa sary amin'ny Label
sary = PhotoImage(file="icon.png")  # Ataovy azo antoka fa eo amin'ny lalana marina ilay fisie
label = Label(fenetre, image=sary)
label.pack(pady=20)

sary_teraka = Image.open("icon.png")  # Alefaso ilay sary tany am-boalohany
sary_voakely = sary_teraka.resize((50, 50))  # Manova ny habeny (50x50 pixels)
sary_tk = ImageTk.PhotoImage(sary_voakely)

# Mampiasa sary amin'ny Button
button = Button(fenetre, image=sary, text="Bouton misy sary", compound="left")
button.pack(pady=20)

fenetre.geometry("300x200")
fenetre.mainloop()
