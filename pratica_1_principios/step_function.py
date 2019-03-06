import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt

freq=1000#numero de amostras para janelamento ??
T=5
N=500
t_array= np.linspace(-T,T,num=N)

def rect(_array):
    x_array=[]
    for element in _array:
        if abs(element)>1/8:
            x_array.append(0)
        elif abs(element)==1/2:
            x_array.append(1/2)
        else:
            x_array.append(1)
    return x_array

def quadratic(t):
    return t**2

plt.subplot(211)
plt.plot(t_array,rect(t_array))

xf=np.linspace(0, 1.0/(2.0*T), N/2)
yf=scipy.fftpack.fft(rect(t_array))

plt.subplot(212)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))


plt.show()

