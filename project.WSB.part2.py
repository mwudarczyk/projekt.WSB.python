from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk

window = Tk()
window.title('Zakładanie nowego konta')
window.geometry('400x700+300+50')
window.configure(bg='#fff')
window.resizable(False, False)

#-------------grafika-----------------
img2 = Image.open('5-kopia 3.png')
resized_img2 = img2.resize((200, 205), Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized_img2)
label2 = Label(window, image=new_pic, bg='white')
label2.pack()

#-------------logowanie-----------------
frame = Frame(window, width=350, height=400)

window.mainloop()