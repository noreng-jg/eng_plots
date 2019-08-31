from pylab import *
from scipy import signal

A=380.14
B=143306.67
C=446490.47

f=logspace(-3,4)
w=2*pi*f
hs=signal.lti([2,0],[1,A,B,C])           #Passa Faixa -> Band Pass
w,mag,phase = signal.bode(hs,w)

figure(1)
subplot(211)
plot(f,mag);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Magnitude(dB)')

subplot(212)
plot(f,phase);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Fase(graus)')

show()
