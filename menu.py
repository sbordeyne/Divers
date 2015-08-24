# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:46:36 2015

@author: Simon
"""

# script lecture_gif.py
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

def Ouvrir():
    Canevas.delete(ALL) # on efface la zone graphique

    filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('gif files','.gif'),('all files','.*')])
    print(filename)

    photo = PhotoImage(file=filename)
    gifdict[filename] = photo  # référence
    print(gifdict)

    Canevas.create_image(0,0,anchor=NW,image=photo)
    Canevas.config(height=photo.height(),width=photo.width())

    Mafenetre.title("Image "+str(photo.width())+" x "+str(photo.height()))

def Fermer():
    Canevas.delete(ALL)
    Mafenetre.title("Image")

def Apropos():
    tkinter.messagebox.showinfo("A propos","Tutorial Python Tkinter\n(C) Fabrice Sincère")

# Main window
Mafenetre = Tk()
Mafenetre.title("Image")

# Création d'un widget Menu
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir une image",command=Ouvrir)
menufichier.add_command(label="Fermer l'image",command=Fermer)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)

# Utilisation d'un dictionnaire pour conserver une référence
gifdict={}

Mafenetre.mainloop()