# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:26:48 2015

@author: Simon
"""

import tkinter as Tkinter

def top():
  fenetre0=Tkinter.Toplevel()
  fenetre0.title("Seconde")

racine0=Tkinter.Tk()
racine0.title("Principale")
bouton0=Tkinter.Button(text="Autre", command=top)
bouton0.pack()
racine0.mainloop()