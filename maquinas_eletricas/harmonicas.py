#!/usr/bin/env python
# coding: utf-8
#Author : V.S.Nörnberg


# # Simulação da Distribuição Espacial da FMM

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.animation import FuncAnimation

sns.set_style('darkgrid')


# Pela expansão de Fourier, podemos decompor uma função harmônica em várias componentes
# No estudo do comportamento da Força magnetomotriz, vemos que ela pode ser representada pela expansão sendo variável com o ângulo espacial formado:
# 
# $$F_{mm}(\theta)=\frac{4}{\pi}\frac{Ni}{2}\displaystyle\sum_{k=1}^n{\frac{(-1)^k cos((1+2k).\theta)}{1+2k}}$$
# 
# A partir desta base tentei compor uma função computacional que retorna o somatório das várias entradas a partir de um dado número de valores entrados:

# In[3]:


def hs(n,theta,ni=50):
    arr=np.array([(k-1)*2 for k in range(1,n+1)])/2
    ns=[]
    for i in arr:
        ns.append((-1)**i*(np.cos((1+i*2)*theta))*(1/(1+2*i))*(ni/2)*(4/np.pi))
    return sum(ns)
    


# # FMM para diferentes harmônicas

# Considerando um valor $Ni =50 A.e $, e simulei como se comporta a força magnetomotriz para diferentes componentes do somatório da representação final.

# ## Visualização da primeira harmônica

# In[38]:


theta=np.linspace(0,2*np.pi,1000)
y=hs(1,theta)
plt.plot(theta, y)
plt.title(r'Força Magnetomotriz com $\theta$ (1 harmônica)')
plt.xlabel(r' $\theta$ (rad)')
plt.ylabel('FMM (A.e)')


# ## Visualização para 8 harmônicas

# In[36]:


theta=np.linspace(0,2*np.pi,1000)
y=hs(8,theta)
plt.plot(theta, y)
plt.title(r'Força Magnetomotriz com $\theta$ (8 harmônicas)')
plt.xlabel(r' $\theta$ (rad)')
plt.ylabel('FMM (A.e)')


# ## Visualização para 10000 harmônicas (próximo a forma quadrada)

# In[35]:


theta=np.linspace(0,2*np.pi,1000)
y=hs(10000,theta)
plt.plot(theta, y)
plt.title(r'Força Magnetomotriz com $\theta$ (10000 harmônicas)')
plt.xlabel(r' $\theta$ (rad)')
plt.ylabel('FMM (A.e)')

# Mostrar   
plt.show()

# Abaixo segue o código para animação gerada da simulação, onde cada frame gerado é um valor instatâneo da corrente alternada variante no tempo. 
# Acabei utilizando um valor intermediário de harmônicas(46)
# É interessante observar que obteu-se um padrão de onda estacionária. O movimento pode ser percebido através do arquivo de vídeo gerado.  

# In[41]:


from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig=plt.figure()


ax=plt.axes(xlim=(0,360),ylim=(-50,50))
plt.title(r'Força Magnetomotriz com $\theta$ (46 harmônicas)')
plt.xlabel(r' $\theta$ (°)')
plt.ylabel('FMM (A.e)')

t=np.linspace(-8,8,1000)
line,=ax.plot([],[],lw=3)

def init():
    line.set_data([],[])
    return line,
   
def animate(i):
    y=hs(46,theta,50*np.sin(2*np.pi*(i-.01*i)))
    line.axes.fill_between(theta*(180/(np.pi)), y,where=y >= 0, facecolor='blue', interpolate=True, label='N')
    line.axes.fill_between(theta*(180/(np.pi)), y,where=y < 0, facecolor='red', interpolate=True, label='S')
    line.axes.legend(('Curva da(s) harmônica(s)', 'Polo Norte','Polo Sul'), loc='upper right')
    #line.axes.title('Força Magnetomotriz com $theta$')
    line.set_data(theta*(180/(np.pi)),y)
    return line,

anim=FuncAnimation(fig,animate,init_func=init,frames=200,interval=20)
anim.save('fmm46.mp4')