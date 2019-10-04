#!/usr/bin/env python
# coding: utf-8
#Author : V.S.Nörnberg


# # Simulação da Distribuição Espacial da FMM

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.animation import FuncAnimation
from math import sqrt, pi
sns.set_style('darkgrid')

def hs(n,theta,ni=50):
    arr=np.array([(k-1)*2 for k in range(1,n+1)])/2
    ns=[]
    for i in arr:
        ns.append((-1)**i*(np.cos((1+i*2)*theta))*(1/(1+2*i))*(ni/2)*(4/np.pi))
    return sum(ns)

theta=np.linspace(0,2*np.pi,1000)

from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig=plt.figure()


ax=plt.axes(xlim=(0,360),ylim=(-2,2))
plt.title(r'Força Magnetomotriz em sist. trifásico com $\theta$ (1° harmônica)')
plt.xlabel(r' $\theta$ (°)')
plt.ylabel('FMM (A.e)')

t=np.linspace(-8,8,1000)
line,=ax.plot([],[],lw=3)

N=4
lines = [plt.plot([], [])[0] for _ in range(N)]

def init():
    
    for line in lines:
        line.set_data([],[])
    
    lines[0].axes.legend(('Resultante','1f','2f','3f'),loc='upper right')
    
    return lines
   
def animate(i):
    #Fases estacionárias
    #Para fase unitária, Amax=pi/2
    y1=hs(1,theta,(pi/2)*np.sin(2*np.pi*(i+.01*i)))
    y2=hs(1,theta+((2*np.pi)/3),(pi/2)*np.sin(2*np.pi*((i+.01*i))+((2*np.pi)/3)))
    y3=hs(1,theta+((4*np.pi)/3),(pi/2)*np.sin(2*np.pi*(i+.01*i)+((4*np.pi)/3)))
    
    #Resultante Viajante
    yr=y1+y2+y3
    
    ondas=[y1,y2,y3,yr]
    
    
    for j,line in enumerate(lines):
        line.set_data(theta*(180/(np.pi)),ondas[j])

        
    return lines

anim=FuncAnimation(fig,animate,init_func=init,frames=500,interval=20)
anim.save('fmm1r.mp4')
