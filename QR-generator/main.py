# @ Naveen Maheswaran
# 2019-1-17
import pyqrcode
from tkinter import *
from tkinter import messagebox


def clicked():
    gen_code = txt.get()
    q = pyqrcode.create(gen_code)
    des=txt2.get()+".png"
    q.png(des,scale=5,module_color="#FFD700",background="#000000")
    messagebox.showinfo('Message ', 'Generation success')


# def gen():


window = Tk()
window.title("QR-Generator")

window.geometry('350x200')
lbl = Label(window, text="Source")

lbl.grid(column=0, row=2)
txt = Entry(window, width=30)

txt.grid(column=1, row=2)

lb2 = Label(window, text="Save As")

lb2.grid(column=0, row=3)
txt2 = Entry(window, width=30)

txt2.grid(column=1, row=3)
btn = Button(window, text="Generate", command=clicked)

btn.grid(column=1, row=5)

window.mainloop()

