# -*-coding:Latin-1 -*
import os


nombre1 = 0
nombre2 = 0
choix = 0
continuer = True

while continuer:
    print("----------Calculatrice----------\n\n")
    choix = menu(1)
    if choix == 0:
        continuer = False
        continue
        
    execution(choix)
    




os.system("pause")