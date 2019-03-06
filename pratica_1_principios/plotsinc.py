import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt

freq=1000
T=5
N=500

t_array= np.linspace(-T,T,num=N)
sig=np.sinc(t_array)

plt.subplot(211)
plt.plot(t_array, sig)

xf=np.linspace(0, 1.0/(2.0*T), N/2)
yf=scipy.fftpack.fft(sig)

plt.subplot(212)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.show()