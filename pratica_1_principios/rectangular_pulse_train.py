from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


freq = 10.0284
Ts = 1/199.8848
N = 8192
t = np.linspace(-200,200,num=4096)
sig=signal.square(2 * np.pi * t, 0.2)
sig_fft = np.fft.fft(sig)/N*2
fft_freq = np.fft.fftfreq(N, Ts)

plt.figure()
plt.plot(t[0:100],sig[0:100])
plt.xlabel('time (S)')
plt.ylabel('amplitude (V)')
plt.grid(True)

plt.figure()
plt.plot(fft_freq[:N//2], abs((sig_fft[:N//2])))
plt.xlabel('frequency (Hz)')
plt.ylabel('amplitude ')
plt.grid(True)


plt.show()