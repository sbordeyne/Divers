# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 15:42:26 2015

@author: Simon Bordeyne
"""
import cv2
import numpy as np
from PIL import Image
from time import strftime

def ComparaisonMatchShapes(image):
    ret=[]
    img1 = cv2.imread('{}.png'.format(image),0)
    grey=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    r, thresh = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
    small = cv2.resize(thresh,(100,100))
    contours,hierarchy = cv2.findContours(small,2,1)
    contourAreas=[]
    for i in range(len(contours)):
        contourAreas.append(cv2.contourArea(contours[i]))
    cnt1 = contours[contourAreas.index(max(contourAreas))]
    for i in range(10):
        img2 = cv2.imread('Models/Model_{}.png'.format(i),0)
        r, thresh2 = cv2.threshold(img2, 127, 255,0)
        small2= cv2.resize(thresh2,(100,100))
        contours,hierarchy = cv2.findContours(small2,2,1)
        cnt2 = contours[0]
        ret.append(cv2.matchShapes(cnt1,cnt2,1,0.0))
        return ret.index(min(ret))
        
def log(message,FirstTime=False):
    message=str(message)
    with open("log.txt","a") as log:
        if FirstTime:
            log.write("\n--------------\n{0}\n--------------\n".format(strftime("%A %d %B %Y %H:%M:%S")))
        else:
            log.write("\n[{}] {}".format(strftime("%H:%M:%S"),message))

def Snapshot(nom="image",photo=False,device=0, extension="png"): #PREND UNE PHOTO
    if photo:
        cam=cv2.VideoCapture(device)
        ret, img = cam.read()
        cv2.imwrite("{}.{}".format(nom,extension),img)
        log("Photo prise.")
        cam.release() #On décharge l'espace mémoire attribué a la caméra specifiée avec "device"
    else:
        img=cv2.imread("{}.{}".format(nom,extension))
        log("Image Lue")
    return img

def GetThresh(image, Canny=False,Manuel=False,Auto=True, threshold=170,cannyparam1=100,cannyparam2=200, ext="png"): #CETTE FONCTION TRANSFORME LA PHOTO EN NOIR ET BLANC
    nom=str()
    if Canny: #Canny Edge Detector est un algorithme de détection de bord
        img=cv2.Canny(image,cannyparam1,cannyparam2)
        log("Image seuillee créée avec Canny")
        nom="canny"
    elif Manuel:
        #Conversion en niveaux de gris et flou
        grey=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(grey,5)
        (threshold,img) = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY) #Seuil manuel
        log("Image seuillee créée. Seuil : {}".format(threshold))
        nom="threshold manuel"
    elif Auto:
        #Conversion en niveaux de gris et flou
        grey=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #blur = cv2.medianBlur(grey,5)
        #Puis en N&B
        img= cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
        log("Image seuillee créée. Seuil : automatique")
        nom="threshold auto"
    cv2.imwrite("{}.{}".format(nom,ext), img)
    return img,nom

def IsolateDigits(img,nom,AireContourMini=100,hmin=50,wmin=20):
    contours,h=cv2.findContours(img, mode=cv2.cv.CV_RETR_CCOMP, method=cv2.cv.CV_CHAIN_APPROX_SIMPLE)
    image_chargee=cv2.imread("{}.png".format(nom))
    NombreDeContours=0
    for cnt in contours:
        if cv2.contourArea(cnt)>=AireContourMini:
            [x,y,w,h] = cv2.boundingRect(cnt)#on associe un rectangle au chiffre
            if h>=hmin and w>=wmin and h<=100 and w<=80:
                NombreDeContours+=1
                RegionOfInterest=image_chargee[y:y+h,x:x+w]
                cv2.imwrite("Digits/Digit_{}.png".format(NombreDeContours), RegionOfInterest)
    log("Nombre de Contours : {}".format(NombreDeContours))
    return NombreDeContours

def GetData(nom, ext="png"):#RECUPERE LES DONNEES DE L'IMAGE ENVOYEE EN PARAMETRES ET RENVOIE LA MATRICE ASSOCIEE
    #On ouvre l'image grace à PIL
    img=Image.open("{}.{}".format(nom,ext))
    log("Image Ouverte avec PIL")
    imgdata=img.getdata()
    larg,haut = img.size
    tab = np.array(imgdata)
    #Mise en forme avec numpy
    matrice=np.reshape(tab, (haut,larg))
    log("Matrice\n{}\nHauteur\t{}\nLargeur\t{}".format(matrice,haut,larg))
    return matrice,haut,larg #On renvoie la matrice de l'image, la hauteur et la largeur