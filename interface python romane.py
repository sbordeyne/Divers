# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 22:25:33 2015

@author: Simon Bordeyne
"""

import tkinter as tk
#import cv2

class Frame(tk.Frame):
    """Main window. Class containing every widget used, and inheriting from tk.Frame"""
    def __init__(self,window, **kwargs):
        tk.Frame.__init__(self,window,width=1024,height=768,**kwargs)
        self.pack(fill=tk.BOTH)
        self.r=tk.IntVar()
        self.r.set(50)
        #Creation des widgets
        self.imageLoad = "bouchonreduit.gif"
        self.image=tk.PhotoImage(file=self.imageLoad)
        tk.Button(self, text ="quit", command=self.Quit).grid(row=0,column=0)
        self.Canvas = tk.Canvas(self, width = self.image.width(), height =self.image.height(), bg ='white')
        self.Canvas.create_image(self.image.width()/2,self.image.height()/2,anchor=tk.CENTER,image=self.image)
        self.rect=self.Canvas.create_rectangle(25-self.r.get(), 25-self.r.get(), 25+self.r.get(), 25+self.r.get(), outline='black')
        self.Canvas.bind('<Motion>',self.hover) #<Motion> or <Enter> ??
        self.Canvas.bind('<Button-1>',self.isolate)
        #self.Canvas.focus_set()
        self.Canvas.grid(row=1,column=0)
        self.spin=tk.Spinbox(self, from_=1,to=500, increment=2, width=10)
        self.spin.config(textvariable=self.r, font="sans 24", justify="center")
        self.spin.grid(row=0,column=1)
    
    def hover(self,event):
        """Function designed to make a cursor sized for the rectangle to isolate"""
        X = event.x
        Y = event.y
        self.Canvas.coords(self.rect,X-self.r.get()/2, Y-self.r.get()/2, X+self.r.get()/2, Y+self.r.get()/2)
        pass
    
    def isolate(self,event):
        """Function designed to cut a square out of the main picture and store it. The file lines are here to increment the filename so 
        that it doesn't overwrite the previous ones"""
        x=int(event.x)
        y=int(event.y)
        imagecv=cv2.imread("bouchonreduit.jpg")
        """f=open("fichier.txt","r")
        line=f.read()
        count=int(line)
        f.close()
        count+=1
        f=open("fichier.txt","w")
        f.write("{}".format(self.count))
        f.close()"""
        RegionOfInterest=imagecv[y-self.r.get()/2:y+self.r.get()/2,x-self.r.get()/2:x+self.r.get()/2]
        cv2.imwrite("result.png", RegionOfInterest)
        pass
    def Quit(self):
        self.quit()
        self.destroy()

window=tk.Tk()
frame=Frame(window)
frame.mainloop()
################"
"""
from math import*
from PIL import Image, ImageTk
from VideoCapture import Device
#import Image
from time import clock
import numpy as np

def h(self,event):
    """"""Function designed to make a cursor sized for the rectangle to isolate""""""
    X = event.x
    Y = event.y
    self.Canvas.coords(self.rect,X-self.r.get()/2, Y-self.r.get()/2, X+self.r.get()/2, Y+self.r.get()/2)
    return [X,Y]

def Capture_data(nom_fichier,infor,infog,infob):
    im= Image.open(nom_fichier)
    L=im.size[0]
    H=im.size[1]
    DATA=[]
    data=list(im.getdata())
    for i in range (L) :
        ligne=[]
        for j in range (H) :
            ftmp = ( infor*1.0*data[i+j*L][0] + infog*1.0*data[i+j*L][1] + infob*1.0*data[i+j*L][2])/(infor+infog+infob)*1.0
            ligne.append(int(ftmp))
        DATA.append(ligne)
    return DATA


def conversion(img) : #convertit les niveaux de gris en float entre 0 et 1
        H, L = img.shape
        imgo = np.array(L*H*[0.])
        imgo = imgo.reshape(H, L)
        for x in range(L) :
                for y in range(H) :
                        imgo[y, x] = float(img[y, x])/256.
        return imgo

def convolution02(Img0,Img1,x,y,X,Y) :
    H, L = Img0.shape[0], Img0.shape[1]
    h, l = Img1.shape[0], Img1.shape[1]
    S = 0.
    for a in range(l) :
            for b in range(h) :
                    c = (a - l/2 + x + X + L)%L
                    d = (b - h/2 + y + Y + H)%H
                    S = S + (float(Img1[b,a]) - float(Img0[d,c]))**2
    return S

def convolution(Img0,Img1,x,y,Delta) : # img1 est la plus petite image. On cherche autour du point (x,y) une ressemblance.
        Img_res = np.array(((2*Delta+1)**2)*[0])
        Img_res = Img_res.reshape((2*Delta+1, 2*Delta+1))
        for a in range(2*Delta+1) :
                for b in range(2*Delta+1) :
                        X = a - Delta
                        Y = b - Delta
                        Img_res[a,b] = convolution02(Img0,Img1,x,y,X,Y)
        return Img_res

def renvoie_i_j_du_min(res) :
        N = len(res)
        P = len(res[0])
        Min = res[0, 0]
        Max = res[0, 0]
        i0, j0 = 0, 0
        for i in range(N) :
                for j in range(P) :
                        if res[i, j] < Min :
                                i0, j0 = i, j
                                Min = res[i, j]
                        if res[i, j] > Max :
                                Max = res[i, j]
        if 1.*Min < Max :
                return [i0-N/2, j0-P/2]
        return [0,0]


X=250
Y=250
img2 = Capture_data("bouchonreduit.jpg",1,1,1)
img3 = Capture_data("result.png",1,1,1)
Delta=20
Z=[]
Z.append( renvoie_i_j_du_min(convolution(img3,img2,X,Y,Delta)))
print Z
""""""
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img3 = conversion(gray)

    # Display the resulting frame
    cv2.imshow('frame',gray)
#    cv2.imshow('frame1',img3)
    if len(img2) > 1 :
        cv2.imshow('frame2',img2)
        Delta = 20
        Z.append( renvoie_i_j_du_min(convolution(img3,img2,X,Y,Delta)))
#    print "key" , cv2.waitKey(1)
    i = -1
    var = cv2.waitKey(1)
    if var & 0xFF == ord('i'):
            print ("x,y depuis le programme principal", X, Y)
    if var & 0xFF == ord('q'):
        break
""""""
print (renvoie_i_j_du_min(convolution(img3,img2,X,Y,Delta)))
"""