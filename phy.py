# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:32:14 2015

@author: Simon
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *

N=10
V_init=np.zeros((N+2,N+2))
seuil = 0.00000001

def carre(V_work,x1,y1,x2,y2,potentiel=4):
    pas_touche=[]    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            V_work[i,j]=potentiel
            pas_touche.append((i,j))
    return V_work,pas_touche
    pass

def laplacien(V_work,i,j):
    return 0.25*(V_work[i+1,j]+V_work[i-1,j]+V_work[i,j+1]+V_work[i,j-1])
    pass

def remplacement(V_work,pas_touche):
    for i in range(1,N):
        for j in range(1,N):
            if V_work[i,j]!=4:#if (i,j) not in pas_touche:
                V_work[i,j]=laplacien(V_work,i,j)
    return V_work
    pass

def comparaison(V_work,pas_touche,seuil):
    V_old=np.copy(V_work)
    V_new=np.copy(V_work)
    V_new=np.copy(remplacement(V_work,pas_touche))
    V_diff=np.copy(V_new-V_old)
    print(V_diff)
    while abs(V_diff).max()>=seuil:
        V_diff=np.copy(V_new-V_old)
        print(abs(V_diff).max())
        V_old=np.copy(V_new)
        V_new=np.copy(remplacement(V_old,pas_touche))
    return V_new
    pass

def trace_surface(V_affiche):
    X,Y=np.meshgrid(np.array(range(V_affiche.shape[0])),np.array(range(V_affiche.shape[1])))
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    surf=ax.plot_surface(X,Y,V_affiche,cmap=cm.coolwarm)
    plt.show()
    pass

def trace_equipotentielles(V_affiche,nb_equi=20):
    X,Y=np.meshgrid(np.array(range(V_affiche.shape[0])),np.array(range(V_affiche.shape[1])))
    Vmin,Vmax=np.min(V_affiche),np.max(V_affiche)
    scale=np.linspace(Vmin,Vmax,nb_equi)
    contour(X,Y,V_affiche,scale)
    plt.axes().set_aspect('equal')
    plt.colorbar()
    pass

V,pas_touche=carre(V_init,2,2,4,4,4)
V_afficher=comparaison(V,pas_touche,seuil)
#trace_surface(V_afficher)
trace_equipotentielles(V_afficher,20)