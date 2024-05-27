from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk

root=Tk()
root.title("Panel logowania/tworzenia konta")
root.geometry("900x500+200+100")
root.configure(bg='linen')
root.resizable(False, False)

def signin():
    username = user.get()
    password = passw.get()

    file=open('baza danych.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())

    if username in r.keys() and password == r[username]:
        screen=Toplevel(root)
        screen.title('WITAJ W PRZESTRZENI WU.STUDIO')
        screen.geometry('900x500+200+100')
        screen.config(bg='linen')
        screen.resizable(False, False)
        Label(screen, text='Witaj na oficjalnej stronie\nWU.STUDIO!',bg='linen',fg='blue', font=('Bauhaus 93', 36)).pack(expand=False)

        #-----Ginger png-----
        img3 = Image.open('ginger.png')
        resized_img3 = img3.resize((220, 300), Image.LANCZOS)
        new_pic = ImageTk.PhotoImage(resized_img3)
        label3 = Label(screen, image=new_pic, bg='linen')
        label3.pack()
        label3.place(x=100, y=120)
        descriptionginger = Label(screen,text='G I N G E R\nto praca akrylowa, na podobraziu bawełnianym,\nzostała namalowana dla przyjaciół pod koniec roku 2023.\nFormat obrazu to 180x130 cm',fg='blue', bg='linen', font=('72 condensed', 10))
        descriptionginger.place(x=70, y=425)

        # -----ULTRA png-----
        img4 = Image.open('ultra.png')
        resized_img4 = img4.resize((220, 300), Image.LANCZOS)
        new_pic2 = ImageTk.PhotoImage(resized_img4)
        label4 = Label(screen, image=new_pic2, bg='linen')
        label4.pack()
        label4.place(x=400, y=120)
        descriptionultra = Label(screen,text='U L T R A\nObraz ten powstał na zamówienie prywatnego klienta.\nBędzie ozdabiał mieszkanie w Krakowie.\nFormat obrazu to 100x150 cm',fg='blue', bg='linen', font=('72 condensed', 10))
        descriptionultra.place(x=370, y=425)

        # -----PORTO png-----
        img5 = Image.open('porto.png')
        resized_img5 = img5.resize((220, 300), Image.LANCZOS)
        new_pic3 = ImageTk.PhotoImage(resized_img5)
        label5 = Label(screen, image=new_pic3, bg='linen')
        label5.pack()
        label5.place(x=600, y=120)
        descriptionporto = Label(screen,text='P O R T O\nTa praca jest moim najnowszym obrazem.\nKlientom zależało na oddaniu Portugalskiego wina Porto.',fg='blue', bg='linen', font=('72 condensed', 10))
        descriptionporto.place(x=500, y=425)

        screen.mainloop()

    else:
        messagebox.showerror('BŁĄD', 'Niepoprawna nazwa uzytkownika lub hasło')

def signup_command():
    window=Toplevel(root)


img = PhotoImage(file='5-kopia 3.png')
Label(root, image=img, bg='linen').place(x=10, y=0)
frame=Frame(root, width=360, height=400, bg='linen')
frame.place(x=500, y=70)

heading=Label(frame, text='Zaloguj do serwisu',fg='blue', bg='linen', font=('Bauhaus 93',26))
heading.place(x=30, y=5)

#------------username----------------
def enter(n):
    user.delete(0, 'end')


def leave(n):
    name=user.get()
    if name == '':
        user.insert(0, 'Nazwa użytkownika')


user = Entry(frame, width=25, fg='blue', border=0, bg='linen', font=('72 Condensed',12))
user.place(x=40, y=85)
user.insert(0, 'Nazwa użytkownika')
user.bind('<FocusIn>', enter)
user.bind('<FocusOut>', leave)
Frame(frame, width=295, height=2, bg='coral').place(x=35,y=110)

#------------password----------------
def enter(n):
    passw.delete(0, 'end')

def leave(n):
    name=passw.get()
    if name == '':
        passw.insert(0, 'Hasło')


passw = Entry(frame, width=25, fg='blue', border=0, bg='linen', font=('72 Condensed',12))
passw.place(x=40, y=155)
passw.insert(0, 'Hasło')
passw.bind('<FocusIn>', enter)
passw.bind('<FocusOut>', leave)
Frame(frame, width=295, height=2, bg='coral').place(x=35,y=180)

#------------login/sign up-----------
Button(frame, width=40, pady=8, text='Wszystko gotowe. Zaloguj', bg='blue', fg='white', border=0, font=('72 Condensed',12), command=signin).place(x=40, y=200)
label=Label(frame,text='Nie masz jeszcze konta?', fg='blue', bg='linen', font=('72 Condensed',10))
label.place(x=80, y=260)

sign_up= Button(frame, width=15, text='kliknij i lecimy!', border=0, bg='linen', cursor='hand2', fg='coral', font=('Bauhaus 93', 10), command=signup_command)
sign_up.place(x=200, y=260)

root.mainloop()