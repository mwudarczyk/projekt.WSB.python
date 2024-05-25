from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Panel logowania/tworzenia konta")
root.geometry("900x500+200+100")
root.configure(bg='#fff')
root.resizable(False, True)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=60, y=60)

frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=500, y=70)

heading=Label(frame, text='Zaloguj do serwisu',fg='#57a1f8', bg='white', font=('Bauhaus 93',26))
heading.place(x=30, y=5)

#------------username----------------
user = Entry(frame, width=25, fg='#57a1f8', border=0, bg='white', font=('72 Condensed',12))
user.place(x=40, y=85)
user.insert(0, 'Nazwa użytkownika')
Frame(frame, width=295, height=3, bg='teal').place(x=35,y=110)

#------------password----------------
password = Entry(frame, width=25, fg='#57a1f8', border=0, bg='white', font=('72 Condensed',12))
password.place(x=40, y=155)
password.insert(0, 'Hasło')
Frame(frame, width=295, height=3, bg='teal').place(x=35,y=180)

Button(frame, width=40, pady=8, text='Wszystko gotowe. Zaloguj', bg='#57a1f8', fg='white', border=0).place(x=40, y=200)
label=Label(frame,text='Nie masz jeszcze konta?', fg='#57a1f8', bg='white', font=('72 Condensed',10))
label.place(x=80, y=260)

sign_up= Button(frame, width=14, text='kliknij i działamy!', border=0, bg='white', cursor='hand2', fg='teal')
sign_up.place(x=200, y=260)

root.mainloop()

