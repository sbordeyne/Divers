import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
from scipy import interpolate
from scipy.interpolate import KroghInterpolator
from math import*

FaCO=[0.172,0.345,0.689,1.03,1.38,2.07,3.45,5.17,6.89]
e=[0.19,0.22,0.26,0.28,0.30,0.34,0.38,0.42,0.44]
Y=[2.30,1.99,1.71,1.55,1.45,1.31,1.15,1.04,1.00]

#question 1

plt.plot(FaCO,e,'.')
plt.plot(FaCO,Y,'.')
plt.show()


#question 2

f = interpolate.interp1d(FaCO,e) #fonction interpolation lineaire
x=np.linspace(0.172,6.89,100)    #on divise l'intervalle en 100 elements
y=f(x)
plt.plot(FaCO,e,'o',x,f(x),'-')   #courbe (FaCO,e) et (x,f(x))
plt.xlabel('FaCO')  #nomme l'axe des x puis apres y
plt.ylabel('e')
plt.title('interpolation_lineaire,e=f(FaCO)')  #on nomme le graphique 
plt.show()    #on affiche 

    
g = interpolate.interp1d(FaCO,Y)
x=np.linspace(0.172,6.89,100)
y=g(x)
plt.plot(FaCO,Y,'o',x,g(x),'-')
plt.xlabel('Y')
plt.ylabel('e')
plt.title('interpolation_lineaire,Y=f(Faco)')
plt.show()
    
    

f = KroghInterpolator(FaCO,e)    #interpolation polynomiale
x=np.linspace(0.172,6.89,100)
y=f(x)
plt.plot(FaCO,e,'o',x,f(x),'-')
plt.xlabel('FaCO')
plt.ylabel('e')
plt.title('interpolation_polynomiale,e=f(FaCO)')
plt.show()

    
g = KroghInterpolator(FaCO,Y)
x=np.linspace(0.172,6.89,100)
y=g(x)
plt.plot(FaCO,Y,'o',x,g(x),'-')
plt.xlabel('Y')
plt.ylabel('e')
plt.title('interpolation_polynomiale,Y=f(Faco)')
plt.show()


f = interpolate.interp1d(FaCO,e,kind='cubic')   #interpolation cubique
x=np.linspace(0.172,6.89,100)
y=f(x)
plt.plot(FaCO,e,'o',x,f(x),'-')
plt.xlabel('FaCO')
plt.ylabel('e')
plt.title('interpolation_cubique,e=f(FaCO)')
plt.show()

    
g = interpolate.interp1d(FaCO,Y,kind='cubic')
x=np.linspace(0.172,6.89,100)
y=g(x)
plt.plot(FaCO,Y,'o',x,g(x),'-')
plt.xlabel('Y')
plt.ylabel('e')
plt.title('interpolation_cubique,Y=f(Faco)')
plt.show()
    

#question 3 

def parametres(r,interpolation):
    
    FaCO=[0.172,0.345,0.689,1.03,1.38,2.07,3.45,5.17,6.89]
    e=[0.19,0.22,0.26,0.28,0.30,0.34,0.38,0.42,0.44]
    Y=[2.30,1.99,1.71,1.55,1.45,1.31,1.15,1.04,1.00]
    
    if interpolation == "lineaire" :
        f = interpolate.interp1d(FaCO,e) 
        g = interpolate.interp1d(FaCO,Y)
   
    if interpolation == "cubique" :        
        f = KroghInterpolator(FaCO,e) 
        g = KroghInterpolator(FaCO,Y)
        
    if interpolation == "cubique" : 
        f = interpolate.interp1d(FaCO,e,kind='cubic')
        g = interpolate.interp1d(FaCO,Y,kind='cubic')
        
        
    e=f(r)
    y=g(r)
    X=1-e*y
    
    return float(e),float(X),float(y)

print (parametres(0.5,"lineaire"))
