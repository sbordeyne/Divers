# -*-coding:Latin-1 -*
import os

nombreDeMultiplications = 12
continuer = True

while continuer:
    
    i = 0 #i sert a parcourir la boucle while
    nombreAMultiplier = int(input("Entrez le nombre correspondant a la table souhaitee    "))
    print("\n\n")
    
    while i <= nombreDeMultiplications:
        print(i , " x ", nombreAMultiplier, " = ", i * nombreAMultiplier)
        i += 1
    
    print("\n\n")
    choix = int(input("Continuer ? (1/0)   "))
    if choix != 1:
        continuer = False
    print("\n\n")


os.system("pause")