# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def u(t):
    E=5
    tau = 0.05
    T=20*tau
    if t>=0 and t<=T/2:
        return E*(1-np.exp(-t/tau))
    elif t>=T/2 and t<=T:
        return E*np.exp(-(t-T/2)/tau)
    else:
        if t>0:
            return u(t-(t//T)*T)
        else:
            return u(t+(np.abs(t)//T+1)*T)

u_2=np.vectorize(u)
t=np.arange(-4.5,4.5,0.001)
plt.plot(t,u_2(t))
plt.axis([-4,4,-0.5,5.5])
plt.xlabel("t (en s)")
plt.ylabel("u(t) (en V)")
plt.title("LA MERE A NATAN")
plt.grid()
plt.show()
plt.close()