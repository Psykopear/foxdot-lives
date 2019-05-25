from FoxDot import *
Scale.default=Scale.phrygian
Clock.clear()

b1 >> evilbass(var([0,0,2,1], 4), dur=PDur(P[3,5,7,4],8), amp=0.5, sus=0.4, oct=(4))
d1 >> play("http://", mix=(0,0.8), room=0.7, rate=P[1,.2,-1,1,-0.2]).often("stutter", 3, dur=2, hpf=500, shape=.2, hpr=0.3)
k1.reset() >> play("X-", sample=2)
s1 >> ambi(b1.degree, shape=P[.0,.1,.2,.3,.4,.5,.6,.7], oct=(4,5,6), amp=PRand([1,0.9,0.8,0.7]), chop=4, dur=0.5, sus=1, pan=PWhite(-1,1), hpf=PWhite(100,1000), hpr=0.2)


Scale.default=Scale.aeolian
d1 >> play("http://", mix=(0,0.8), room=0.7, rate=P[1,.2,-1,1,-0.2]).often("stutter", 3, dur=2, hpf=500, shape=.2, hpr=0.3)
k1.reset() >> play("X-X-X-p", sample=2)
b1.reset() >> dbass(0, dur=1,sus=1,  amp=.8, lpf=300, lpr=0.3)
