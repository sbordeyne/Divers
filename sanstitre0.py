# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:26:12 2015

@author: Simon
"""
import cv2
def Snapshot(nom="image",photo=True,device=1, extension="png"): #PREND UNE PHOTO
    if photo:
        cam=cv2.VideoCapture(device)
        ret, img = cam.read()
        cv2.imwrite("{}.{}".format(nom,extension),img)
        cam.release() #On décharge l'espace mémoire attribué a la caméra specifiée avec "device"
    else:
        img=cv2.imread("{}.{}".format(nom,extension))
    return img
