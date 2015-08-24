# -*- coding: cp1252 -*-
import cv2

def Snapshot(nom="image",device=0): #PRENDS UNE PHOTO
    cam=cv2.VideoCapture(device)
    ret, img = cam.read()
    cv2.imwrite("{}.png".format(nom),img)
    #On désalloue la mémoire
    cam.release()
    return img


img=Snapshot()
