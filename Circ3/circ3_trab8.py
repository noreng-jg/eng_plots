from pylab import *
from scipy import signal

A=5
B=8

f=logspace(-2,3)
w=2*pi*f

############      Declaração das funções de Transf

vpa=signal.lti([1,0,0],[1,A,B])         #Passa Alta -> High Pass
vpf=signal.lti([1],[1,A,B])             #Passa Baixa   -> Low pass
vpb=signal.lti([1,0],[1,A,B])           #Passa Faixa -> Band Pass

wa,maga,phasea = signal.bode(vpa,w)
wf,magf,phasef = signal.bode(vpf,w)
wb,magb,phaseb = signal.bode(vpb,w)

###########      PLOT VPA     ################
figure(1)
subplot(211)
plot(w,maga);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Magnitude(dB)')

subplot(212)
plot(w,phasea);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Fase(graus)')
###########        PLOT VPF     ###############

figure(2)
subplot(211)
plot(w,magf);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Magnitude(dB)')

subplot(212)
plot(w,phasef);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Fase(graus)')

###########             PLOT VPB        ###############
figure(3)
subplot(211)
plot(w,magb);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Magnitude(dB)')

subplot(212)
plot(w,phaseb);xscale('log');xlabel('Frequencia(Rad/S)');ylabel('Fase(graus)')


show()


