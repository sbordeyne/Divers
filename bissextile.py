# -*-coding:Latin-1 -*
import os 
annee = int(input("Saisissez une annee : "))
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'annee saisie est bissextile.")
else:
    print("L'annee saisie n'est pas bissextile.")
os.system("pause")