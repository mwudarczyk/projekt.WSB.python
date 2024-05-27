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
        Label(screen, text='Witaj na oficjalnej stronie\nWU.STUDIO!',bg='linen',fg='blue', font=('Bauhaus 93', 36)).pack(expand=False)

        # -----Ginger png-----
        img3 = Image.open('ginger.png')
        resized_img3 = img3.resize((220, 300), Image.LANCZOS)
        new_pic = ImageTk.PhotoImage(resized_img3)
        label3 = Label(screen, image=new_pic, bg='linen')
        label3.pack()
        label3.place(x=60, y=120)
        descriptionginger = Label(screen,text='G I N G E R\nto praca akrylowa, na podobraziu bawełnianym,\nzostała namalowana dla przyjaciół pod koniec roku 2023.\nFormat obrazu: 180x130 cm',fg='blue', bg='linen', font=('72 condensed', 9))
        descriptionginger.place(x=40, y=425)

        # -----ULTRA png-----
        img4 = Image.open('ultra.png')
        resized_img4 = img4.resize((220, 300), Image.LANCZOS)
        new_pic2 = ImageTk.PhotoImage(resized_img4)
        label4 = Label(screen, image=new_pic2, bg='linen')
        label4.pack()
        label4.place(x=345, y=120)
        descriptionultra = Label(screen,text='U L T R A\nObraz ten powstał na zamówienie prywatnego klienta.\nBędzie ozdabiał mieszkanie w Krakowie.\nFormat obrazu: 100x150 cm',fg='blue', bg='linen', font=('72 condensed', 9))
        descriptionultra.place(x=335, y=425)

        # -----PORTO png-----
        img5 = Image.open('porto.png')
        resized_img5 = img5.resize((220, 300), Image.LANCZOS)
        new_pic3 = ImageTk.PhotoImage(resized_img5)
        label5 = Label(screen, image=new_pic3, bg='linen')
        label5.pack()
        label5.place(x=620, y=120)
        descriptionporto = Label(screen,text='P O R T O\nTa praca jest moim najnowszym obrazem.\nKlientom zależało na oddaniu Portugalskiego wina Porto.\nFormat obrazu: 150x150 cm',fg='blue', bg='linen', font=('72 condensed', 9))
        descriptionporto.place(x=610, y=425)

        screen.mainloop()

    else:
        messagebox.showerror('BŁĄD', 'Niepoprawna nazwa uzytkownika lub hasło')

#-------------------------------------FORMULARZ TWORZENIA KONTA------------------------------------------
def signup_command():
    window=Toplevel(root)
    window.title('Zakładanie nowego konta')
    window.geometry('400x600+300+50')
    window.configure(bg='linen')
    window.resizable(False, False)


    def signup():
        username = user.get()
        password = passw.get()
        password2 = passw2.get()
        if password == password2:
            try:
                file=open('baza danych.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('baza danych.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('ZACZYNAMY', 'Konto założone pomyślnie :)')
                window.destroy()

            except:
                file = open('baza danych.txt', 'w')
                pp = str({'username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('BŁĄD', 'Hasła nie są zgodne. Spróbuj ponownie :(')

    def sign():
        window.destroy()


    #-------------grafika-----------------
    img2 = Image.open('5-kopia 3.png')
    resized_img2 = img2.resize((200, 200), Image.LANCZOS)
    new_pic = ImageTk.PhotoImage(resized_img2)
    label2 = Label(window, image=new_pic, bg='linen')
    label2.pack()

    #-------------logowanie-----------------
    frame = Frame(window, width=300, height=600, bg='linen')
    frame.place(x=50, y=200)
    heading = Label(frame, text='Tworzenie nowego konta', fg='blue', bg='linen', font=('Bauhaus 93', 18))
    heading.place(x=20, y=1)

    description = Label(frame, text='Witam cię w mojej artystycznej strefie!\nBardzo mi miło, że mnie odwiedzasz :)\nNa tej stronie znajdziesz informacje o moich obrazach\noraz kilka słów ode mnie. Enjoy', fg='coral', bg='linen', font=('72 condensed', 10))
    description.place(x=20, y=310)

    #-------------Uzytkownik-----------------
    def enter(n):
        user.delete(0, 'end')

    def leave(n):
        if user.get() == '':
            user.insert(0, 'Nazwa użytkownika')


    user = Entry(frame, width=30, fg='blue', border=0, bg='linen', font=('72 Condensed', 12))
    user.place(x=30, y=50)
    user.insert(0, 'Nazwa użytkownika')
    user.bind('<FocusIn>', enter)
    user.bind('<FocusOut>', leave)
    Frame(frame, width=250, height= 2, bg='coral').place(x=30, y=70)

    #-------------HASŁO-----------------
    def enter(n):
        passw.delete(0, 'end')

    def leave(n):
        if passw.get() == '':
            passw.insert(0, 'Hasło')


    passw = Entry(frame, width=30, fg='blue', border=0, bg='linen', font=('72 Condensed', 12))
    passw.place(x=30, y=110)
    passw.insert(0, 'Hasło')
    passw.bind('<FocusIn>', enter)
    passw.bind('<FocusOut>', leave)
    Frame(frame, width=250, height= 2, bg='coral').place(x=30, y=130)

    #-------------POTWIERDZENIE-----------------
    def enter(n):
        passw2.delete(0, 'end')

    def leave(n):
        if passw2.get() == '':
            passw2.insert(0, 'Powtórz hasło')


    passw2 = Entry(frame, width=30, fg='blue', border=0, bg='linen', font=('72 Condensed', 12))
    passw2.place(x=30, y=170)
    passw2.insert(0, 'Powtórz hasło')
    passw2.bind('<FocusIn>', enter)
    passw2.bind('<FocusOut>', leave)
    Frame(frame, width=250, height= 2, bg='coral').place(x=30, y=190)

    #-------------adres email-----------------
    def enter(n):
        mail.delete(0, 'end')

    def leave(n):
        if mail.get() == '':
            mail.insert(0, 'Podaj swój adres e-mail')


    mail = Entry(frame, width=30, fg='blue', border=0, bg='linen', font=('72 Condensed', 12))
    mail.place(x=30, y=230)
    mail.insert(0, 'Podaj swój adres e-mail')
    mail.bind('<FocusIn>', enter)
    mail.bind('<FocusOut>', leave)
    Frame(frame, width=250, height= 2, bg='coral').place(x=30, y=250)

    #------------przyciski------------------
    Button(frame, width=20, pady=2, text='Zaczynamy!', bg='blue', fg='white', border=0, font=('Bauhaus 93', 10), command=signup).place(x=135, y=270)
    signin = Button(frame, width=15, text='Jednak mam konto', border=0, bg='linen', cursor='hand2', fg='blue', font=('72 Condensed', 8, 'bold'), command=sign).place(x= 35, y=270)

    window.mainloop()

#-----------------------------KONIEC KODU FORMULARZA TWORZENIA NOWEGO KONTA------------------------------

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