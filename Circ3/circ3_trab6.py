from pylab import *
from scipy import signal


def HS():
    args=[158434572.92419],[1,18322.930231821,158434414.48978]
    return args

f=logspace(-2,7)
w=2*pi*f

tf=signal.lti(HS()[0],HS()[1])
w,mag,phase=signal.bode(tf,w)
figure(1)
subplot(211)
plot(f,mag);xscale('log')
subplot(212)
plot(f,phase);xscale('log')



show()
