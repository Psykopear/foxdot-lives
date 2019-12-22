Clock.clear()

from FoxDot import *
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s1 >> feel([0]*10+[3, 3, 2, 2, 1, 1], chop=1, dur=0.5, oct=(4,5), sus=0.15, amp=(1,1), shape=(PWhite(0.1,0.2),0))


b1 >> sawbass(s1.degree, sus=0.2, amp=PEuclid(P[12,9,11,5].shuffle().palindrome(),16)*2, dur=0.25)

k1 >> play("X{[- ][--][ -]-}", sample=2, amp=1.0)

m.hpf=0;m.hpr=0.3
m.lpf=0;m.lpr=0.3
