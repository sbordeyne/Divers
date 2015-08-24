from tkinter import *
from time import sleep

def updatetext(event):
    var.set(e.get())
    root.update_idletasks()

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

e = Entry(root)
e.pack()
e.bind(sequence='<KeyRelease>', func=updatetext)

root.mainloop()
