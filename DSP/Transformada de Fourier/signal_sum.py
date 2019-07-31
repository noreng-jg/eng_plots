#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from matplotlib import pyplot as plt
from numpy import cos, pi

#vetor de tempo
t=np.linspace(0,10,2000)

#sinal com velocidade angular caracterizada por 2.pi.f
def sinal(t,f):
    return cos(2*pi*f*t)
    
s1=sinal(t,400)
s2=sinal(t,600)

plt.subplot(211)

plt.plot(t,s1)

plt.subplot(212)

plt.plot(t,s2)

plt.show()

plt.plot(t,s1)
plt.plot(t,s2)
plt.plot(t,s1+s2)
plt.show()
# Pelo algoritmo da FFT, temos que discretamente cada reposta $y[k]$ associasse a cada elemento da sequência $x[n]$ pela seguinte forma:

# $y[n]=\displaystyle\sum_{n=0}^{N-1} {e^{-2 \pi  j.\frac{k . n}{N}}. x[n]}$

# obs: Usando o formato grande do somatório fica \displayformat.

# In[5]:


from scipy.fftpack import fft


# In[14]:


N=2000

#espaçamento de amostra
ts=1/2800

x=np.linspace(0,N*ts,N)
y=sinal(x,400)+sinal(x,600)

#Apenas o lado positivo das frequâncias
yf=fft(y)
xf=np.linspace(0.0,1/(2*ts),N//2)


plt.plot(xf,(2.0/N)*np.abs(yf[0:N//2]))

plt.grid()
plt.show()


# In[ ]:




