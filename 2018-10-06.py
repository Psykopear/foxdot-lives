FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
Root.default=var((PIndex()*4)%7,128,start=now)
m = Master()

k1 >> play("V[--]", sample=5, amp=3.2, shape=(0,0.1), room=(0,0.7), mix=(0,0.5))
n1 >> noise(amp=linvar([0,1],16,start=now), lpr=0.2, lpf=linvar([0,10000],16,start=now), dur=0.25, sus=0.5, mix=0.8, room=0.8, oct=6).stop()
d1 >> play("<|h2| ><{[  ]-}-*{[--]-}>", formant=var([4, 0], [8, inf], start=now)).sometimes("amen")
b2 >> dbass(var([0,PRand([0,1,-2,1,-1])],4), oct=var([5,(5,6)], [12,4]), lpf=3700, lpr=0.2, sus=0.8, dur=PDur(P[7,5,7,11],16), amp=0.9)
s2 >> prophet(b2.degree, sus=4, dur=4, oct=(5,6), chop=(8,16), formant=(4,0), shape=(0,0.4))
s3 >> viola(s2.degree, dist=1, shape=1, oct=(4,5), lpr=0.2, lpf=4000, dur=PDur(P[3,5],8), chop=2)
Group(d1,s3,b2).solo()
SynthDefs
