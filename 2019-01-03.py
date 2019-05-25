FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

b1 >> evilbass(var([0,3,2,-1],[10,5,2,3]), dur=PDur(var([3],8),8), oct=4, sus=sinvar([0.2,0.9],32), cutoff=sinvar([100,5000],16), amp=1, shape=(0,0.2), room=0.4, mix=(0,1)).spread()
d1 >> play("s", dur=PDur(P[7,5,9],10), sample=PRand(list(range(5))), hpf=PWhite(100,4000), hpr=0.3, delay=PRand([0,0,0,0.01,0.015,-0.01,-0.015]), room=0.2, mix=0.3, amp=PWhite(0.8,1.2))
k1 >> play("XsX X X X ", sample=2, amp=1, room=0.4, mix=(0,0.6)).often("stutter", 2.5, dur=2)
s1 >> scatter(b1.degree, shape=sinvar([0,0.7],50), formant=PWhite(0,1), dur=1/1.25, oct=4, amp=16)
SynthDefs
