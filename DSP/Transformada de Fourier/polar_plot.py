#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np

import matplotlib.pyplot as plt

theta=np.arange(0,2*np.pi,0.001)

def cos(t,f):
    return np.cos(2*np.pi*f*t)    

#Mudando a frequência e visualizando 
#sua representação no plano complexo
#com coordenadas polares.

plt.subplot(2,2,1,projection='polar')
plt.plot(theta,cos(theta,0.3))

plt.subplot(2,2,2,polar=True)
plt.plot(theta,cos(theta,0.4))

plt.subplot(2,2,3,polar=True)
plt.plot(theta,cos(theta,0.8))

plt.subplot(2,2,4,polar=True)
plt.plot(theta,cos(theta,0.6366))

plt.show()


# In[7]:


plt.subplot(polar=True)
plt.plot(theta,cos(theta,0.1591))

plt.show()
# In[14]:


for i in [0,2*np.pi/4,2*np.pi/2,2*np.pi*(3/4),2*np.pi]:
    plt.axvline(x=i,linestyle='--',color='r')
    
plt.plot(theta,cos(theta,0.1591))  
plt.show()

# In[58]:


plt.subplot(polar=True)
freq=0.1591


angles= [0,2*np.pi/4,2*np.pi/2,2*np.pi*(3/4),2*np.pi]

for angle in angles:
    plt.plot(angle, cos(angle,freq),'ro')

plt.plot(0,-0.4, 'gx')#localiação aproximada do centroide da figura...
        
plt.plot(theta,cos(theta,freq))  


plt.show()



