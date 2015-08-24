# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 16:11:40 2015

@author: Simon
"""

import cv2

fr=open("fichier.txt","r")
ligne=fr.read()
i=int(ligne)
i+=1
fw=open("fichier.txt","w")
fw.write("{}".format(i))
fw.close()
fr.close()
tennis=cv2.imread("tennis.jpg")
#cv2.imshow("lol",tennis)
x=int(input("x?\t"))
y=int(input("y?\t"))
RegionOfInterest=tennis[y:y+50,x:x+50]
cv2.imwrite("tennis{}.png".format(i), RegionOfInterest)