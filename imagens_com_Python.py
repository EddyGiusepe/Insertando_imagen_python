from tkinter import Label, PhotoImage, Tk


root = Tk()
root.geometry("1200x1000")
root.config(bg="orange")


imagen = PhotoImage(file="3.png")
fondo = Label(root, image=imagen).place(
    x=300, y=20, width="1200", height="1000")


root.mainloop()
