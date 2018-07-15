from FoxDot import *

Scale.default=Scale.chromatic

Root.default=var([0,0,0,0],[8,8,8,8])

s1 >> klank((0, P[5,5,5,5,4,4,4,4], 9), room=0.5, oct=(4,5), mix=0.3, dur=2, sus=2)


b1 >> sawbass(P[0,0,0,0, 4,0,0,0, 2,0,0,0, -2,0,0,0], dur=0.25, sus=0.1, cutoff=900, rq=0.2, formant=PWhite(1,2), amp=2)

d1 >> play("<X(- [--]-)><  Oo><=   >", sample=2, amp=(1,0.5,1))


s2 >> pluck(b1.degree, dur=0.125, chop=PRand([1,2,0.5]), hpf=PWhite(1000,2000), hpr=0.2, shape=0.3, amp=1.2)


Group(s2,s1).mix=1
Group(s2,s1,b1).amplify=expvar([0,1],0.5)*expvar([0,1],0.5)
