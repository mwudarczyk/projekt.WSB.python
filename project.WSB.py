from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Panel logowania/tworzenia konta")
root.geometry("900x600+200+100")
root.configure(bg='#fff')
root.resizable(True, True)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=60, y=60)

frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=500, y=70)

heading=Label(frame, text='Zaloguj do serwisu',fg='#57a1f8', bg='white', font=('Bauhaus 93',26))
heading.place(x=30, y=5)

user = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Bauhaus 93',12))
user.place(x=60, y=80)

root.mainloop()

