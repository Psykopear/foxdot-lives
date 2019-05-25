FoxDot.start

from FoxDot import *

Clock.clear()
Scale.default=Scale.lydianAug
Root.default=var(P[0], 1)
m = Master()
m.amplify=var([1,1],[28,4], start=now)
g = Group(k2, b1)
g.amplify=var([1,0],[28,4])

SynthDefs

(
    s1 >> pasha(P[0,0,0,0,1,1,2,2,-1,-2,-3,3,0,0].shuffle().mirror().mirror(), hpr=0.2, hpf=PWhite(400,800), oct=(4,5,6), dur=PDur(P[3,5,4,6],8), sus=0.2, chop=PRand([2]), amp=0.8),
    k1 >> play("--*o", amp=PWhite(0.8,1.2), mix=0.3, room=0.3),
    k2 >> play("X ", hpr=0.1, hpf=0, sample=2, room=(0,0.4), mix=0.9, amp=(1.1, 0.4)),
    # k2 >> play("[XXXX]", hpr=0.1, hpf=200, sample=2, room=(0,0.4), mix=0.9, amp=(1.1, 0.4)),
    b1 >> evilbass(s1.degree, amp=0.5, dur=PDur(P[4,6],8), sus=0.7, oct=(4)),
)
