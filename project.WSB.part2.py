from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk

window = Tk()
window.title('Zakładanie nowego konta')
window.geometry('400x700+300+50')
window.configure(bg='linen')
window.resizable(False, False)

#-------------grafika-----------------
img2 = Image.open('5-kopia 3.png')
resized_img2 = img2.resize((200, 200), Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized_img2)
label2 = Label(window, image=new_pic, bg='linen')
label2.pack()

#-------------logowanie-----------------
frame = Frame(window, width=300, height=390, bg='linen')
frame.place(x=50, y=200)
heading = Label(frame, text='Tworzenie nowego konta', fg='blue', bg='linen', font=('Bauhaus 93', 18))
heading.place(x=20, y=1)

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

window.mainloop()