from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Zaloguj się")
root.geometry("900x600+200+100")
root.configure(bg='#fff')
root.resizable(True, True)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=60, y=60)

root.mainloop()

#zmiana zmiana