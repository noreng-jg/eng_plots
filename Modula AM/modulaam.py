import numpy as np
import matplotlib.pyplot as plt

k=0.5
n=1000000
fm=2000
fcarrier=20000

T=0.001

t=np.linspace(0,n*T,n)
m=np.sin(2*np.pi*fm*t)
carrier= np.sin(2*np.pi*fcarrier*t)
s=carrier*(1+k*m)


plt.figure()
plt.plot(t,m)
plt.xlabel('time (S)')
plt.ylabel('amplitude (V)')
plt.grid(True)

plt.figure()
plt.plot(t,carrier)
plt.xlabel('time (S)')
plt.ylabel('amplitude (V)')
plt.grid(True)
plt.figure()
plt.plot(t,s)
plt.xlabel('time (S)')
plt.ylabel('amplitude (V)')
plt.grid(True)


#---Teorema da amostragem -------
# ---periodo de amostragem deve ser no máximo 1/2W

ts=1.0/(2*40000.0)

#--onde W = largura de banda da portadora 2*fcarrier

tf=np.linspace(0,n*ts,n)
m=np.sin(2*np.pi*fm*tf)
carrier= np.sin(2*np.pi*fcarrier*tf)
s=carrier*(1+k*m)
plt.figure()
S=np.fft.fft(s)
f=np.fft.fftfreq(n,ts)
F=np.fft.fftshift(f)
splot=np.fft.fftshift(S)
plt.plot(F,1.0/n*np.abs(S))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.grid(True)


plt.show()