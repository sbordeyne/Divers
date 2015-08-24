# -*-coding:Latin-1 -*
import os
from math import fabs

def menu(type = 1):
    print("\n\n")
    if type == 1:
        choix = menu1()
    elif type == 2:
        choix = menu2()
    elif type == 3:
        choix = menu3()
    else:
        choix = 0
return choix

def menu1():
    print("1 : Addition\n2 : Soustraction\n3 : Division\n 4 : Multiplication\n")
    while choix != 1 or choix != 2 or choix != 3 or choix != 4
        choix = fabs(int(input("\nQuel est votre choix ?\t")))
    return choix